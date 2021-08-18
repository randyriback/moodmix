import os
from dotenv import load_dotenv

secret = "gHxzQE9CCqCK01BHf87jBr4BR_tm6ya3"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variables for the flask app.
    Using Env. variables where available
    Otherwise create the config variable if not done already
    """

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')


    SECRET_KEY = os.environ.get('SECRET') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sqlaclchemy