

class BaseConfig(object):
    DATABASE = {
        'name': 'poyntz.db',
        'engine': 'peewee.SqliteDatabase'
    }

    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DATABASE = {
        'name': 'test_run.db',
        'engine': 'peewee.SqliteDatabase'
    }

    DEBUG = True
    TESTING = True
    