
from service.school_service import school_search_service


def search_schools(text):
    sr = school_search_service.search_schools(text, 3)
    print('Results for "{}" (search took: {}s)'.format(text, sr.time_taken))
    for i, r in enumerate(sr.results):
        print("{}. {}".format(i+1, r.name))
        print("{}, {}".format(r.city, r.state))

if __name__ == '__main__':
    search_schools("elementary school highland park")
