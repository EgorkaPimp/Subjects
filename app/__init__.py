from flask import Flask
from .extensions import db
from config import Config


config_class = Config

app = Flask(__name__)

app.config.from_object(config_class)

db.init_app(app)

from app import routers  # noqa: E402, F401

with app.app_context():
    db.create_all()


