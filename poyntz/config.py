

class BaseConfig(object):
    DATABASE = {
        'name': 'poyntz.db',
        'engine': 'peewee.SqliteDatabase'
    }

    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # FLASK_RUN_PORT = 5000
    # FLASK_RUN_HOST = '0.0.0.0'
    EXPLAIN_TEMPLATE_LOADING = False


class TestConfig(BaseConfig):
    DATABASE = {
        'name': 'test_run.db',
        'engine': 'peewee.SqliteDatabase'
    }

    DEBUG = True
    TESTING = True
    