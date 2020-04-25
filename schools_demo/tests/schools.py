import unittest

from service.school_service import school_search_service


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.school_search_service = school_search_service

    def test_overload_exception(self):
        text = "elementary school highland park"
        with self.assertRaises(Exception):
            self.school_search_service.search_schools(text, 100)

    def test_search_num_results(self):
        text = "elementary school highland park"
        for num_results in range(1, 10):
            sr = self.school_search_service.search_schools(text, num_results)
            self.assertTrue(len(sr.results), num_results)

    def test_school_with_city(self):
        text = "jefferson belleville"
        sr = self.school_search_service.search_schools(text, 1)
        self.assertTrue('JEFFERSON' in sr.results[0].name)
        self.assertEqual('BELLEVILLE', sr.results[0].city)
        self.assertEqual('IL', sr.results[0].state)

    def test_school_exact_name(self):
        text = 'riverside school 44'
        sr = self.school_search_service.search_schools(text, 1)
        self.assertEqual('RIVERSIDE SCHOOL 44', sr.results[0].name)
        self.assertEqual('INDIANAPOLIS', sr.results[0].city)
        self.assertEqual('IN', sr.results[0].state)

    def test_school_approximate_search(self):
        text = 'granada charter school'
        sr = self.school_search_service.search_schools(text, 2)
        school_names = [s.name for s in sr.results]
        self.assertTrue('NORTH VALLEY CHARTER ACADEMY' in school_names)
        self.assertTrue('GRANADA HILLS CHARTER HIGH' in school_names)
        cities = [s.city for s in sr.results]
        self.assertTrue(len(set(cities)) == 1)
        self.assertEqual('GRANADA HILLS', cities[0])

    def test_school_with_state_name(self):
        text = 'foley high alabama'
        sr = self.school_search_service.search_schools(text, 1)
        self.assertEqual('FOLEY HIGH SCHOOL', sr.results[0].name)
        self.assertEqual('FOLEY', sr.results[0].city)
        self.assertEqual('AL', sr.results[0].state)

    def test_school_upper_case(self):
        text = 'KUSKOKWIM'
        sr = self.school_search_service.search_schools(text, 2)
        self.assertEqual(len(sr.results), 1)
        self.assertEqual('TOP OF THE KUSKOKWIM SCHOOL', sr.results[0].name)
        self.assertEqual('NIKOLAI', sr.results[0].city)
        self.assertEqual('AK', sr.results[0].state)

    def test_school_containing_city_name(self):
        text = "chicago elementary"
        sr = self.school_search_service.search_schools(text, 1)
        self.assertEqual('CHICAGO PARK ELEMENTARY', sr.results[0].name)
        self.assertEqual('GRASS VALLEY', sr.results[0].city)
        self.assertEqual('CA', sr.results[0].state)


if __name__ == '__main__':
    unittest.main()
