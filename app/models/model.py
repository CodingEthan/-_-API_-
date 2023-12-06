import sys
from flask_sqlalchemy import SQLAlchemy
from app.router import app

# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     SQLALCHEMY_COMMIT_TEARDOWN = True

db = SQLAlchemy(app)