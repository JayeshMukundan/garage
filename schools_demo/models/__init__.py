from utils.constants import LOCATION_TYPE_CITY
from utils.constants import LOCATION_TYPE_MLOCALE
from utils.constants import LOCATION_TYPE_STATE
from utils.constants import STATE_NAMES


class School():
    def __init__(self, id, name, operating_agency, city, state, mlocale, ulocale):
        self.id = id
        self.name = name
        self.operating_agency = operating_agency
        self.city = city
        self.state = state
        self.state_name = STATE_NAMES[state]
        self.mlocale = mlocale
        self.ulocale = ulocale
        self.key = '__'.join([id, name, city, state, mlocale, ulocale])

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

class LocationSummary():
    def __init__(self, location_type, location_name, location_count):
        self.location_type = location_type
        self.location_name = location_name
        self.location_count = location_count

class LocationSummaryCollection():
    def __init__(self):
        self.location_collection = {}
        self.location_collection[LOCATION_TYPE_STATE] = []
        self.location_collection[LOCATION_TYPE_CITY] = []
        self.location_collection[LOCATION_TYPE_MLOCALE] = []

    def add_summary(self, location_summary):
        self.location_collection[location_summary.location_type].append(location_summary)

    def total_count(self):
        return sum(ls.location_count for ls in self.location_collection[LOCATION_TYPE_STATE])

    def get_schools_count_by(self, location_type):
        if location_type not in self.location_collection:
            raise Exception("Given location type {} isn't supported".format(location_type))
        return self.location_collection[location_type]

class SearchResult():
    def __init__(self):
        self.results = []
        self.time_taken = None
