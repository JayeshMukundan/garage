

def setup_routes(app):
    from application.routes.auth.google_oauth import register_google_oauth_routes
    from application.routes.apis import register_authorized_routes
    register_google_oauth_routes(app)
    register_authorized_routes(app)