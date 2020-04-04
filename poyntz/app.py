from flask import Flask, abort

from flask_peewee.db import Database

from . import config


app = Flask(__name__)
app.config.from_object(config)
db = Database(app)
