import os
import sys

from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TestTable1(Base):
    __tablename__ = 'test_table_1'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    string_col1 = Column(String(250), nullable=False)
    string_col2 = Column(String(250), nullable=False)
    int_col1 = Column(Integer, nullable=False)

class TestTable2(Base):
    __tablename__ = 'test_table_2'

    id = Column(Integer, primary_key=True)
    int_col1 = Column(Integer, nullable=False)
    date_col1 = Column(Date, nullable=False)
    fk_col_1 = Column(Integer, ForeignKey('test_table_1.id'), nullable=False)
    fk_col_1_obj = relationship(TestTable1, foreign_keys=[fk_col_1])
    string_col1 = Column(String(1000), nullable=False)

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)
