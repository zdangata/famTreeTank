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
    birthday = db.Column(db.Date, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Children', backref='Tanko', lazy=True)
    bio = db.Column(db.String(1000), nullable=True)
    
    def __init__(self, name, birthday, marital_status, children, bio):
        self.name = name
        self.birthday = date_of_birth
        self.marital_status = marital_status
        self.children = children
        self.bio = bio

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.birthday,
            'marital_status': self.marital_status,
            'children': self.children,
            'bio': self.bio
        }

class Children(db.Model):
    __tablename__ = 'Children'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Grandchildren', backref='Children', lazy=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Tanko.id'))
    bio = db.Column(db.String(1000), nullable=True)

    def __init__(self, name, birthday, marital_status, children, parent_id, bio):
        self.name = name
        self.birthday = date_of_birth
        self.marital_status = marital_status
        self.children = children
        self.parent_id = parent_id
        self.bio = bio

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.birthday,
            'marital_status': self.marital_status,
            'children': self.children,
            'parent_id': self.parent_id,
            'bio': self.bio
        }

class Grandchildren(db.Model):
    __tablename__ = 'Grandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    marital_status = db.Column(db.String, nullable=True)
    children = db.relationship('Greatgrandchildren', backref='GrandChildren', lazy=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Children.id'))
    bio = db.Column(db.String(1000), nullable=True)

    def __init__(self, name, birthday, marital_status, children, parent_id, bio):
        self.name = name
        self.birthday = date_of_birth
        self.marital_status = marital_status
        self.children = children
        self.parent_id = parent_id
        self.bio = bio

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.birthday,
            'marital_status': self.marital_status,
            'children': self.children,
            'parent_id': self.parent_id,
            'bio': self.bio
        }

class Greatgrandchildren(db.Model):
    __tablename__ = 'Greatgrandchildren'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('Grandchildren.id'))
    bio = db.Column(db.String(1000), nullable=True)

    def __init__(self, name, birthday, parent_id, bio):
        self.name = name
        self.birthday = date_of_birth
        self.parent_id = parent_id
        self.bio = bio

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birthname': self.birthday,
            'parent_id': self.parent_id,
            'bio': self.bio
        }