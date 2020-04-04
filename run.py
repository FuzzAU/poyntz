from poyntz.app import app, db
from poyntz import models
from poyntz.views import *


def create_tables():
    db.database.create_tables([models.Point])


if __name__ == '__main__':
    create_tables()
    app.run()