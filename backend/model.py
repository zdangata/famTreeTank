from flask import Flask, request, Response, abort
from flask_sqlalchemy import SQLAlachemy
from flask_migrate import Migrate
from config import *
import json
import os

app = Flask(__name__)
database_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy()