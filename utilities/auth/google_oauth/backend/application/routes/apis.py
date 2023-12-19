from flask_jwt_extended import jwt_required, get_jwt_identity

from application.addons.jwt import JWTAddon


def register_authorized_routes(app):
    @app.route('/api/say_hello')
    @jwt_required()
    def say_hello():
        current_user = get_jwt_identity()
        return f"Hello, {current_user}! This is a protected resource."

    @app.route('/api/logout')
    @jwt_required()
    def logout():
        jti = get_jwt_identity()
        JWTAddon.invalidate_jwt_token(jti)
        return 'Logout successful'
