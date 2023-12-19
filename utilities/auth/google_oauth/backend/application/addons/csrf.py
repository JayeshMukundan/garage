from flask_wtf.csrf import CSRFProtect
def setup_csrf(app):
    CSRFProtect(app)