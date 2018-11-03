from flask import Flask
from config import Config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'everything is magic'
app.config.from_object(Config)

from app import routes