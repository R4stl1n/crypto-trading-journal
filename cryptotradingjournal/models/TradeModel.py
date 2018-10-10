from peewee import *
from app import db

class TradeModel(db.Model):

    exchange = IntegerField()
    exit_date = DateTimeField(null=False)
    entry_date = DateTimeField(null=False)
    primary_coin = CharField()
    secondary_coin = CharField()
    direction = IntegerField()
    entry_price = DoubleField(null=False)
    exit_price = DoubleField(null=False)
    fee_cost = DoubleField(null=False)
    pnl = DoubleField(null=False)
    amount = DoubleField(null=False)
    profitable = BooleanField(default=False)
    gross_profit = DoubleField(null=False)
    net_profit = DoubleField(null=False)