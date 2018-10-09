from peewee import *
from flask_security import RoleMixin

from app import db

class RoleModel(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)