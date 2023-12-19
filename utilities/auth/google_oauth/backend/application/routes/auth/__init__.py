from abc import ABC, abstractmethod
from application.addons.database import db
from application.models import User
class AuthFazade():

    def login(self, user):
        ...

    def logout(self, user):
        ...

    def register(self, user):
        db.session.add(user)
        db.session.commit()
        self.login(user)

auth_fazade = AuthFazade()