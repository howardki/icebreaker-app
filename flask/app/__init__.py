from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'everything is magic'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///icebreaker.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)
db.app = app
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models
