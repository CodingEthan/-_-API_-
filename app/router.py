from flask import Flask, request, url_for, session, jsonify, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ccb211202@localhost:3306/ccb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from app.route import user
