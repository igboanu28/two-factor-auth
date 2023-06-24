import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'who-are-you'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Uche_123@localhost/two_factor'

    SQLALCHEMY_TRACK_MODIFICATION = False