from time import perf_counter_ns

from data_store.reader import reader
from models import LocationSummary
from models import LocationSummaryCollection
from models import School
from models import SearchResult
from utils.constants import LOCATION_TYPE_CITY
from utils.constants import LOCATION_TYPE_MLOCALE
from utils.constants import LOCATION_TYPE_STATE
from utils.constants import MAX_SEARCH_RESULTS
from utils.performance_utils import measure_time_in_seconds


class SchoolSearchService():
    CACHE_KEY_NAME = 'name'
    CACHE_KEY_OTHER_LOCATION = 'other_location'
    CACHE_KEY_CITY = 'city'
    CACHE_KEY_CITY_SPLIT = 'city_split'
    SEARCH_NAME_CACHE_KEYS = [CACHE_KEY_NAME]
    SEARCH_LOCATION_CACHE_KEYS = [CACHE_KEY_OTHER_LOCATION, CACHE_KEY_CITY_SPLIT]
    ALL_CACHE_KEYS  = [CACHE_KEY_NAME, CACHE_KEY_CITY, CACHE_KEY_OTHER_LOCATION, CACHE_KEY_CITY_SPLIT]

    def __init__(self):
        self.schools_search_cache = None
        self.schools_loaded = False
        self.states = set()
        self.cities = set()
        self.mlocales = set()
        self._load_schools()

    def _build_metadata(self, schools):
        states = set()
        cities = set()
        mlocales = set()
        for school in schools:
            states.add(school.state)
            cities.add(school.city)
            mlocales.add(school.mlocale)
        self.states = states
        self.cities = cities
        self.mlocales = mlocales

    def _build_search_cache(self, schools):
        schools_cache = {}
        for ck in SchoolSearchService.ALL_CACHE_KEYS:
            schools_cache[ck] = {}
        for school in schools:
            cache_keys = {
                SchoolSearchService.CACHE_KEY_NAME : school.name.lower().split(),
                SchoolSearchService.CACHE_KEY_OTHER_LOCATION: [school.state.lower(), school.state_name.lower(), school.mlocale.lower()],
                SchoolSearchService.CACHE_KEY_CITY: [school.city.lower()],
                SchoolSearchService.CACHE_KEY_CITY_SPLIT: school.city.lower().split(),
            }
            for ckn, ckparts in cache_keys.items():
                for part in ckparts:
                    if part not in schools_cache[ckn]:
                        schools_cache[ckn][part] = []
                    schools_cache[ckn][part].append(school)
        self.schools_search_cache = schools_cache

    def _load_schools(self):
        if not self.schools_loaded:
            schools = reader.read_data()
            self._build_search_cache(schools)
            self._build_metadata(schools)
            self.schools_loaded = True

    def _add_to_summary_collection(self, lsc, location_type, location_info):
        for name, count in location_info.items():
            location_summary = LocationSummary(location_type, name, count)
            lsc.add_summary(location_summary)

    def get_school_stats(self):
        """
        Returns school summary by various locations (state, city and mlocale)
        :return:
        """
        by_state = {state : len(self.schools_search_cache[SchoolSearchService.CACHE_KEY_OTHER_LOCATION][state.lower()]) for state in self.states}
        by_mlocale = {mlocale: len(self.schools_search_cache[SchoolSearchService.CACHE_KEY_OTHER_LOCATION][mlocale.lower()]) for mlocale in self.mlocales}
        by_city = {city: len(self.schools_search_cache[SchoolSearchService.CACHE_KEY_CITY][city.lower()]) for city in self.cities}
        lsc = LocationSummaryCollection()
        self._add_to_summary_collection(lsc, LOCATION_TYPE_STATE, by_state)
        self._add_to_summary_collection(lsc, LOCATION_TYPE_CITY, by_city)
        self._add_to_summary_collection(lsc, LOCATION_TYPE_MLOCALE, by_mlocale)
        return lsc

    def _search_schools(self, parts, cache_keys, schools_already_picked_for_parts={}):
        schools_match_cnt = {}
        num_parts = len(parts)
        schools_picked_for_parts = {}
        schools_picked_for_parts.update(schools_already_picked_for_parts)
        for part in parts:
            for cache_key in cache_keys:
                for school in self.schools_search_cache[cache_key].get(part, []):
                    if school in schools_picked_for_parts.get(part, set()):
                        continue
                    if school not in schools_match_cnt:
                        schools_match_cnt[school] = 1
                    else:
                        schools_match_cnt[school] += 1
                    if part not in schools_picked_for_parts:
                        schools_picked_for_parts[part] = set([school])
                    else:
                        schools_picked_for_parts[part].add(school)

        schools_with_exact_match = []
        for school, cnt in schools_match_cnt.items():
            if cnt == num_parts:
                schools_with_exact_match.append(school)
        return schools_with_exact_match, schools_match_cnt, schools_picked_for_parts

    def search_schools(self, search_text, num_results):
        """
        Search schools for the given text. Removes the skip words (like 'school')
        :param search_text: the text to search for. <str>
        :param num_results: number of results to return. <int>
        :return: SearchResult
        """
        if num_results > MAX_SEARCH_RESULTS:
            raise Exception("Please be nice and ask only for what you need. You can ask for a maximum of {} schools in the search results".format(MAX_SEARCH_RESULTS))

        t1_start = perf_counter_ns()
        # Remove zero value items from the search text
        search_text = search_text.replace(",", '').lower().replace('school', '')
        parts = search_text.split()

        # First look for schools with exact match on the name
        schools_with_exact_match, schools_name_match_cnt, schools_picked_for_parts = self._search_schools(parts, SchoolSearchService.SEARCH_NAME_CACHE_KEYS)
        schools_found = schools_with_exact_match

        # If enough schools aren't found, then look for match on location
        if len(schools_found) < num_results:
            _, schools_location_match_cnt, _ = self._search_schools(parts, SchoolSearchService.SEARCH_LOCATION_CACHE_KEYS, schools_picked_for_parts)
            schools_match_cnt = schools_name_match_cnt
            schools_found_set = set(schools_found)
            for school, cnt in schools_location_match_cnt.items():
                if school in schools_found_set:
                    continue
                if school not in schools_match_cnt:
                    schools_match_cnt[school] = 0

                schools_match_cnt[school] += cnt

            for school in sorted(schools_match_cnt, key=schools_match_cnt.get, reverse=True):
                if school in schools_found_set:
                    continue
                schools_found.append(school)
                if len(schools_found) == num_results:
                    break
        else:
            schools_found = schools_found[:num_results]

        # Construct the response
        sr = SearchResult()
        sr.results = schools_found
        t1_stop = perf_counter_ns()
        sr.time_taken = measure_time_in_seconds(t1_start, t1_stop)
        return sr



school_search_service = SchoolSearchService()
