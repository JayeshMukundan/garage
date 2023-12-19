from flask import Flask
from application.addons import register_addons


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    with app.app_context():
        register_addons(app)

    return app
