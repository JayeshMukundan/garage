def register_addons(app):
    from .auth import setup_oauth
    from .csrf import setup_csrf
    from .database import setup_db
    from .jwt import setup_jwt
    from .login import setup_login
    from .routes import setup_routes
    setup_csrf(app)
    setup_db(app)
    setup_jwt(app)
    setup_login(app)
    setup_oauth(app)
    setup_routes(app)
