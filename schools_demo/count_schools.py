from time import perf_counter_ns

from service.school_service import school_search_service
from utils.constants import LOCATION_TYPE_CITY
from utils.constants import LOCATION_TYPE_MLOCALE
from utils.constants import LOCATION_TYPE_STATE
from utils.performance_utils import measure_time_in_seconds


def _print_location_summary(location_summaries):
    for ls in location_summaries:
        print("{}: {}".format(ls.location_name, ls.location_count))

def _max_schools_info(location_summaries):
    name = None
    cnt = None
    for ls in location_summaries:
        if cnt is None or cnt < ls.location_count:
            name = ls.location_name
            cnt = ls.location_count
    return name, cnt

def print_counts():
    t1_start = perf_counter_ns()
    school_summary = school_search_service.get_school_stats()
    t1_stop = perf_counter_ns()
    print("Time to load data in seconds:", measure_time_in_seconds(t1_start, t1_stop))
    t1_start = perf_counter_ns()
    total_count = school_summary.total_count()
    states_count = school_summary.get_schools_count_by(LOCATION_TYPE_STATE)
    cities_count = school_summary.get_schools_count_by(LOCATION_TYPE_CITY)
    mlocale_count = school_summary.get_schools_count_by(LOCATION_TYPE_MLOCALE)

    print("Total Schools:{}".format(total_count))
    print("Schools by State:")
    _print_location_summary(states_count)
    print("Schools by Metro-centric locale:")
    _print_location_summary(mlocale_count)
    city, max_count = _max_schools_info(cities_count)
    print("City with most schools: {} ({} schools)".format(city, max_count))
    print("Unique cities with at least one school: {}".format(len(cities_count)))
    t1_stop = perf_counter_ns()
    print("Time to extract summary in seconds:", measure_time_in_seconds(t1_start, t1_stop))


if __name__ == '__main__':
    t1_start = perf_counter_ns()
    print_counts()
    t1_stop = perf_counter_ns()
    print("Elapsed time during the whole program in seconds:", measure_time_in_seconds(t1_start, t1_stop))
