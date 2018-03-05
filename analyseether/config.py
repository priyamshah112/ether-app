import os
basedir = os.path.abspath(os.path.dirname(__file__))
# enviornment variables are defined in app.yaml


class ProductionConfig(object):
    # Configurations for development enviornment
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_PROD_DATABASE_URI']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']

    # mail settings
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USE_TLS = os.environ['MAIL_USE_TLS']
    MAIL_USE_SSL = os.environ['MAIL_USE_SSL']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    # mail accounts
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']

class StagingConfig(object):
    # Configurations for staging enviornment
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_STAGE_DATABASE_URI']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']

    # mail settings
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = os.environ['MAIL_PORT']
    MAIL_USE_TLS = os.environ['MAIL_USE_TLS']
    MAIL_USE_SSL = os.environ['MAIL_USE_SSL']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    # mail accounts
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']
