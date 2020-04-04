import peewee
import datetime

from flask_peewee.auth import BaseUser
from .app import db


class Point(db.Model, BaseUser):
    awarded_date = peewee.DateField(default=datetime.datetime.now, null=False)
    category = peewee.TextField(null=False)
    point_type = peewee.TextField(null=False)

    class Meta:
        indexes = (
            (('awarded_date', 'category'), True),
        )

    def __unicode__(self):
        return '{} = {} @ {}'.format(self.category, self.point_type, self.awarded_date)
