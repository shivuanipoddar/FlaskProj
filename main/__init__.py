from flask import Flask
from flask_pymongo import PyMongo


fapp = Flask(__name__)

fapp.secret_key = 'Shivani_secret_key'
mongodb_client = PyMongo(fapp, uri="mongodb://localhost:27017/flask_db")
db = mongodb_client.db


def create_app():
    from FlaskProj.main.routes import app
    fapp.register_blueprint(app)
    return fapp