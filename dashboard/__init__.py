import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Corona(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer,primary_key = True)
    country = db.Column(db.String(30),unique=True,index=True)
    deaths = db.Column(db.Integer)
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    active = db.Column(db.Integer)
    updated = db.Column(db.String(10))
    
    def __init__(self,country,deaths,confirmed,recovered,active,updated):
        self.country = country
        self.deaths = deaths
        self.confirmed = confirmed
        self.recovered = recovered
        self.active = active
        self.updated = updated

    def __repr__(self):
         return f"country {self.country}"
