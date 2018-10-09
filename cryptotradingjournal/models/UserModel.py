from peewee import *
from flask_security import UserMixin

from app import db

class UserModel(db.Model, UserMixin):
    email = TextField()
    username = CharField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)