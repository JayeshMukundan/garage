from application.utils.lang_utils import classproperty
from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity


class JWTAddon:
    _jwt = None
    jwt_revoked_tokens = set()
    @classproperty
    def jwt(cls):
        return cls._jwt

    @classmethod
    def invalidate_jwt_token(cls, jti):
        cls.jwt_revoked_tokens.add(jti)

    @classmethod
    def is_token_revoked(cls, jwt_headers, jwt_payload):
        jti = jwt_payload['jti']
        return jti in cls.jwt_revoked_tokens

def setup_jwt(app):
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    JWTAddon._jwt = JWTManager(app)
    JWTAddon._jwt.token_in_blocklist_loader(JWTAddon.is_token_revoked)

