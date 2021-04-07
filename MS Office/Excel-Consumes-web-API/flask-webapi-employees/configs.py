import os

class Config(object):
    SECURITY_KEY = 'you will never guess'

    # Confugurations for FLASK-SQLALCHEMY
    # SQLALCHEMY_DATABASE_URI = os.environ['MSSQL_URI']
    SQLALCHEMY_DATABASE_URI = r'sqlite:///D:\my-documents\Sample Database\employees.db' # using sqlite database
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DBConfig():
    pass


class DevConfig(Config):
    DEBUG = True


class PrdConfig(Config):
    DEBUG = False


config = {
    'PRD': PrdConfig,
    'DEV': DevConfig
}
