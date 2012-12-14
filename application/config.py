class Config(object):
    DEBUG = False
    TESTING = False
    ASSETS_DEBUG = False
    MONGODB_DB = 'app'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'root'
    MONGODB_PASSWORD = ''
    SECRET_KEY = ''


class ProductionConfig(Config):
    MONGODB_DB = 'app'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'root'
    MONGODB_PASSWORD = ''
    SECRET_KEY = ''


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = ''


class TestingConfig(Config):
    TESTING = True
