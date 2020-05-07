from db.orm import dbInterface
from db.tables import TestTable1

tt1a = TestTable1(string_col1="Hello", string_col2="World", int_col1=125)
tt1b = TestTable1(string_col1="Haya", string_col2="World", int_col1=125)
dbInterface.create_object(tt1a)
dbInterface.create_object(tt1b)
