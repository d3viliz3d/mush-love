from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


FLASK_APP = 'app'
FLASK_ENV = environ.get('FLASK_ENV')
SECRET_KEY = environ.get('SECRET_KEY')

# Flask-Assets
LESS_BIN = environ.get('LESS_BIN')
ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

# Static Assets
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
