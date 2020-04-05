import sys
from flask import Flask, abort

from flask_peewee.db import Database
from poyntz import models

from . import config


def create_tables():
    db.database.create_tables([models.Point])


runtime_config = None
if 'pytest' in sys.modules:
    runtime_config = config.TestConfig
else:
    runtime_config = config.BaseConfig


app = Flask(__name__)
app.config.from_object(runtime_config)
db = Database(app)
