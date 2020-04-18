import sys
from flask import Flask, abort
from flask_peewee.db import Database
from . import config


# Decide on which config to use
runtime_config = None
if 'pytest' in sys.modules:
    runtime_config = config.TestConfig
else:
    runtime_config = config.DevelopmentConfig

app = Flask('__name__',
            static_url_path='',
            static_folder='poyntz/static/',
            template_folder='poyntz/templates/')
app.config.from_object(runtime_config)
db = Database(app)


from poyntz import models

def create_tables():
    # TODO: Probably should move this function
    db.database.create_tables([models.Point])
