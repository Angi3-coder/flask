from flask import Flask
from models import Students, db


app = Flask(__name__)

#configure our app
#tell flask where our database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#disable track modification (recommended setting)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#INITIALIZE db with app
db.init_app(app)

#create database and tables
with app.app_context():
    db.create_all() # creates the tables

print ("database created")