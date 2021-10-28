import os

class Config():
    REGISTERED_USERS = {
    'eros@gmail.com':{"name":"Eduardo","password":"123"},
    'ltav@gmail.com':{"name":"Livael","password":"abc"},
    'gmol@gmail.com':{"name":"Guy","password":"qwerty"}
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
