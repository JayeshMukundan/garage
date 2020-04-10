import os
import sys

from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    work_email = Column(String(250), nullable=False)
    personal_email = Column(String(250), nullable=False)
    work_phone_number = Column(String(15), nullable=False)
    personal_phone_number = Column(String(15), nullable=False)


class BrowniePoints(Base):
    __tablename__ = 'brownie_points'

    id = Column(Integer, primary_key=True)
    points = Column(Integer, nullable=False)
    effective_date = Column(Date, nullable=False)
    giver_profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    giver_profile = relationship(Profile, foreign_keys=[giver_profile_id])
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    profile = relationship(Profile, foreign_keys=[profile_id])
    comments = Column(String(1000), nullable=False)

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)
