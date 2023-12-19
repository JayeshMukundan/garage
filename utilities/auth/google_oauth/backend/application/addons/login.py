from application.utils.lang_utils import classproperty
from flask_login import LoginManager


class LoginAddon:
    _login_manager = None

    @classproperty
    def login_manager(cls):
        return cls._login_manager

def setup_login(app):
    LoginAddon._login_manager = LoginManager(app)
