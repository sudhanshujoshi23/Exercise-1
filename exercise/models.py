from exercise import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Fund(db.Model):
    FundID = db.Column(db.Integer, primary_key=True)
    FundName = db.Column(db.String(50), unique=True, nullable=False)
    UnitPrice = db.Column(db.Float)

    def __repr__(self):
        return f"User('{self.FundName}', '{self.UnitPrice}')"

class Investor(db.Model):
    InvestorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.InvestorID}', '{self.FirstName}', '{self.LastName}', '{self.email}' )"


class Investment(db.Model):
    InvestmentID = db.Column(db.Integer, primary_key=True)
    Fund_ID = db.Column(db.Integer, db.ForeignKey('fund.FundID'), nullable=False)
    Investor_ID = db.Column(db.Integer, db.ForeignKey('investor.InvestorID'), nullable=False)
    Units = db.Column(db.Integer, nullable=False)
