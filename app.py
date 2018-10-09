import os
import sys

from flask import Flask
from flask import render_template
from flask_peewee.db import Database
from flask_security import Security
from flask_security import PeeweeUserDatastore
from flask_security import login_required


base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,
    static_folder=os.path.join(base_dir, 'static'),
    template_folder=os.path.join(base_dir, 'templates'))

app.config.from_object('appconfig.Configuration')

db = Database(app)

from cryptotradingjournal.blueprints.DashboardBlueprint import dashboard_bp

from cryptotradingjournal.models.UserModel import UserModel
from cryptotradingjournal.models.RoleModel import RoleModel
from cryptotradingjournal.models.UserRolesModel import UserRolesModel


user_datastore = PeeweeUserDatastore(db, UserModel, RoleModel, UserRolesModel)

security = Security(app, user_datastore)

app.register_blueprint(dashboard_bp)

@app.before_first_request
def first_run():
    for Model in (RoleModel, UserModel, UserRolesModel):
        Model.create_table(fail_silently=True)
    try:
        UserModel.get_by_id(1)
    except:
        user_datastore.create_user(email='admin@admin.com', password='admin', username="admin")

@app.route('/')
@login_required
def index():
    return render_template('private/dashboard.html')


