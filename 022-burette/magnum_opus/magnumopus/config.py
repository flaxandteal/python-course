import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///:memory:')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PANTRY_STORE = os.environ.get('MAGNUMOPUS_PANTRY_STORE', 'sqlalchemy')
