from flask import Flask, request, Response, abort
from flask_sqlalchemy import SQLAlachemy
from flask_migrate import Migrate
from config import *
import json
import os

app = Flask(__name__)
database_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Database Setup
#----------------------------------------------------------------------------#

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#