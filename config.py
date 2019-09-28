import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    dflt_restaurant_db = 'sqlite:///' + os.path.join(basedir, 'restaurant_db.sqlite')
    SQLALCHEMY_DATABASE_URI = os.environ.get('RESTAURANT_DB_URI') or dflt_restaurant_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False