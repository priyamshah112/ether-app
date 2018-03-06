import os
basedir = os.path.abspath(os.path.dirname(__file__))
# enviornment variables are defined in app.yaml


class ProductionConfig(object):
    # Configurations for production enviornment
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_PROD_DATABASE_URI']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']

    # mail settings
    MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
    MAILGUN_API_URL = os.environ['MAILGUN_API_URL']
    MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']


class StagingConfig(object):
    # Configurations for staging enviornment
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_STAGE_DATABASE_URI']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']

    # mail settings
    MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
    MAILGUN_API_URL = os.environ['MAILGUN_API_URL']
    MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']
