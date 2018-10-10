from flask import request
from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask_security import login_required

trades_bp = Blueprint('trades_bp', __name__, template_folder='templates')

@trades_bp.route('/trades')
@login_required
def trades_view():
    return render_template('private/trades.html')

@trades_bp.route('/addtrade', methods=['POST'])
@login_required
def add_trade_view():
    entryDate = request.form['entryDate']
    exitDate = request.form['exitDate']
    exchange = request.form['exchange']
    coinPair = request.form['coinPair']
    entryPrice = request.form['entryPrice']
    exitPrice = request.form['exitPrice']
    fee = request.form['fee']
    quantity = request.form['quantity']
    isLong = request.form['long']
    tradeNotes = request.form['tradeNotes']