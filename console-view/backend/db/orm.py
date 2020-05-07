from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.class_utils import get_class_for_name

from .tables import Base


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

    def get_by_id(self, cls_name, id):
        cls = get_class_for_name(cls_name)
        with self.session_scope() as session:
            return list(session.query(cls).filter_by(id=id))[0]

    def create_object(self, obj):
        with self.transactional_session_scope() as session:
            session.add(obj)

dbInterface = DBInterface()
