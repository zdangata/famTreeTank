from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *
import os

app = Flask(__name__)
database_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy()

migrate = Migrate(app, db)
#----------------------------------------------------------------------------#
# Database Setup
#----------------------------------------------------------------------------#

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Tanko(db.Model):
    __tablename__ = 'Tanko'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Children', backref='Tanko', lazy=True)
    bio = db.Column(db.String(1000), nullable=True)
    
    def __repr__(self):
        return f'<Tanko {self.id} {self.name} {self.dOB} {self.marital_status} {self.children} {self.bio}>'

class Children(db.Model):
    __tablename__ = 'Children'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Grandchildren', backref='Children', lazy=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Tanko.id'), nullable=False)
    bio = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<Children {self.id} {self.name} {self.dOB} {self.marital_status} {self.children} {self.parent_id} {self.bio}>'

class Grandchildren(db.Model):
    __tablename__ = 'Grandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Greatgrandchildren', backref='GrandChildren', lazy=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Children.id'), nullable=False)
    bio = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<Children {self.id} {self.name} {self.dOB} {self.marital_status} {self.children} {self.parent_id} {self.bio}>'

class Greatgrandchildren(db.Model):
    __tablename__ = 'Greatgrandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dOB = db.Column(db.DateTime, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Grandchildren.id'), nullable=False)
    bio = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<Children {self.id} {self.name} {self.dOB} {self.parent_id} {self.bio}>'