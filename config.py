from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app, origins=[
    "https://frontend-baseball.onrender.com",  
    "http://localhost:5173"
])
#Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitch_data.db'
#Disable track modifications to save resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
