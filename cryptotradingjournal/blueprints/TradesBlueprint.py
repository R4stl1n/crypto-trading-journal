from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask_security import login_required

trades_bp = Blueprint('trades_bp', __name__, template_folder='templates')

@trades_bp.route('/trades')
@login_required
def trades_view():
    return render_template('private/trades.html')