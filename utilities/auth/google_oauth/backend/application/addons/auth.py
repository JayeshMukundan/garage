from application.utils.lang_utils import classproperty
from datetime import timedelta
from flask_oauthlib.client import OAuth

class AuthAddon:
    _oauth = None

    @classproperty
    def oauth(cls):
        return cls._oauth

def setup_oauth(app):
    AuthAddon._oauth = OAuth(app)
