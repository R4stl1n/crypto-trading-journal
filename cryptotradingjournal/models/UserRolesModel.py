from peewee import *

from app import db

from cryptotradingjournal.models.UserModel import *
from cryptotradingjournal.models.RoleModel import *

class UserRolesModel(db.Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(UserModel, related_name='roles')
    role = ForeignKeyField(RoleModel, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)