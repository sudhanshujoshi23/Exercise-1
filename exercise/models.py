from exercise import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    # db.Model for the Users Table
     id = db.Column(db.Integer, primary_key=True)
     public_id = db.Column(db.Integer)
     Name = db.Column(db.String(50))
     email = db.Column(db.String(120), unique=True, nullable=False)
     password = db.Column(db.String(50))
     admin = db.Column(db.Boolean)

class Fund(db.Model):
    # db.Model for the Fund Table
    FundID = db.Column(db.Integer, primary_key=True)
    FundName = db.Column(db.String(50), unique=True, nullable=False)
    UnitPrice = db.Column(db.Float)

    def __repr__(self):
        return f"Fund('{self.FundName}', '{self.UnitPrice}')"

class Investor(db.Model):
    # db.Model for the Investor Table
    InvestorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fund_value = db.relationship('Investment', backref='Investor')
    
    def __repr__(self):
        return f"Investor('{self.InvestorID}','{self.FirstName}')"

class Investment(db.Model):
    # db.Model for the Investment Table
    InvestmentID = db.Column(db.Integer, primary_key=True)
    Fund_ID = db.Column(db.Integer, db.ForeignKey('fund.FundID'), nullable=False)
    Investor_ID = db.Column(db.Integer, db.ForeignKey('investor.InvestorID'), nullable=False)
    Units = db.Column(db.Integer, nullable=False)
    Investment_Value = db.Column(db.Integer)
    
    def __repr__(self):
        return f'{self.Investment_Value}'
