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

class Tanko(db.Tanko):
    __tablename__ = 'Tanko'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.Column(db.String, nullable=True)
    bio = db.Column(db.String(1000), nullable=True)
    

class Children(db.Children):
    __tablename__ = 'Children'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = 
    bio = db.Column(db.String(1000), nullable=True)

class Grandchildren(db.Grandchildren):
    __tablename__ = 'Grandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = 
    parents = 
    bio = db.Column(db.String(1000), nullable=True)

class Greatgrandchildren(db.Greatgrandhildren):
    __tablename__ = 'Greatgrandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = 
    parents = 
    bio = db.Column(db.String(1000), nullable=True)