from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables import Base, BrowniePoints, Profile


class DBInterface():
    def __init__(self):
        self.engine = create_engine('sqlite:///sqlalchemy_example.db')
        Base.metadata.bind = self.engine
        self.dbSession = sessionmaker(bind=self.engine)

    @contextmanager
    def transactional_session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.dbSession()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def session_scope(self):
        session = self.dbSession()
        try:
            yield session
        finally:
            session.close()

    def create_profile(self, profile):
        with self.transactional_session_scope() as session:
            session.add(profile)

    def create_brownie_points(self, browniePoint):
        with self.transactional_session_scope() as session:
            session.add(browniePoint)

    def get_all_profiles(self):
        with self.session_scope() as session:
            return list(session.query(Profile).all())

    def get_all_brownie_points(self, profile_id):
        with self.session_scope() as session:
            return list(session.query(BrowniePoints).filter_by(profile_id=profile_id))


dbInterface = DBInterface()
