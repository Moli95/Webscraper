from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis
from rq import Queue

app = Flask(__name__)

app.config.from_envvar('APP_SETTINGS')
app.config['TESTING'] = app.config['DEBUG'],
db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column(db.String, primary_key=True, unique=True,)
    website_url = db.Column(db.Text)
    used_method = db.Column(db.Text)
    created_at = db.Column(db.Text)
    result = db.Column(db.Text)

db.create_all()

r = redis.Redis()
q = Queue(connection=r)

from app import views
from app import tasks
