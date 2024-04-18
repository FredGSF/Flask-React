from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

## connection to database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

## tracking modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## data base instance
db = SQLAlchemy(app)
