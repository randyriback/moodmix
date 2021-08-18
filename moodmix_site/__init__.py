from flask import Flask
from flask.json import JSONEncoder
from config import Config
from .app.routes import mm

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder



app = Flask(__name__)

app.register_blueprint(mm)

app.config.from_object(Config)



root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
app.json_encoder = JSONEncoder

import models

CORS(app)

with app.app_context():
    if root_db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, root_db, render_as_batch=True)
    else:
        migrate.init_app(app, root_db)