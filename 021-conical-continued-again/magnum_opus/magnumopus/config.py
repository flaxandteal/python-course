import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:////tmp/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
