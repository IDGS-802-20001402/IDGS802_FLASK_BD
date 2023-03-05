import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    # mysql connection
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = create_engine('mysql://root@localhost:3306/idgs802').url
    SQLALCHEMY_TRACK_MODIFICATIONS = False