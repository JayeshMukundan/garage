from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from application.utils.lang_utils import classproperty

db = SQLAlchemy()
class DBAddon:
    _db = None
    @classproperty
    def db(cls):
        return cls._db

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    DBAddon._db = db
    db.init_app(app)
    Migrate(app, db)
    from application.models import User
