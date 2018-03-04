import os
basedir = os.path.abspath(os.path.dirname(__file__))
# enviornment variables are defined in app.yaml


class ProductionConfig(object):
    # Configurations for development enviornment
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(['SQLALCHEMY_PROD_DATABASE_URI'])
    SECURITY_PASSWORD_SALT = os.environ.get(['SECURITY_PASSWORD_SALT'])


class StagingConfig(object):
    # Configurations for staging enviornment
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_STAGE_DATABASE_URI']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
