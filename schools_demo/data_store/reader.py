import csv

from models import School
from utils.constants import SCHOOLS_FILE


class Reader():
    def read_data(self):
        raise NotImplementedError("Implement in the derived class")


class CsvReader(Reader):
    def read_data(self):
        with open(SCHOOLS_FILE, encoding='ISO-8859-1') as csvfile:
            rows_reader = csv.reader(csvfile, delimiter=',')
            next(rows_reader)
            schools = []
            for row in rows_reader:
                state = 'DC' if row[5] == 'C' else row[5]
                school = School(row[0], row[3], row[2], row[4], state, row[8], row[9])
                schools.append(school)
        return schools

reader = CsvReader()
