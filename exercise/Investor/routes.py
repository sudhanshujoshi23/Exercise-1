from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from exercise import db
from exercise.Investor.forms import Create_Investor, Add_Investment
from exercise.models import Fund, Investment, Investor, Users


investors = Blueprint('investors', __name__)


@investors.route("/Investors", methods=['GET','POST'])
@login_required
def Investors():
    # List all the investor
    Investors = Investor.query.all()
    invested_sums = {}
    for investor in Investors:
        invested_sums[investor.InvestorID] = 0
        investments_by_investor = Investment.query.filter_by(Investor_ID=investor.InvestorID)
        for investment in investments_by_investor:
            invested_sums[investor.InvestorID] += investment.Investment_Value
    return render_template('Investors.html', title="List of Investors", investors=Investors, invested_sums=invested_sums) 

@investors.route("/Investor/New", methods=['GET','POST'])
@login_required
def create_investor():
    # Create a new investor.
    form = Create_Investor()
    if form.validate_on_submit():
        investor = Investor(FirstName = form.FirstName.data, LastName = form.LastName.data, email = form.Email.data)
        db.session.add(investor)
        db.session.commit()
        flash('Investor created in the Database.', 'success')
        return redirect(url_for('investors.Investors'))
    return render_template('Create_Investor.html', title='Add a new Investor', form=form)

@investors.route("/Investor/<int:Investor_ID>/update", methods=['GET','POST'])
@login_required
def update_investor(Investor_ID):
    # Update an existing investor
    investor = Investor.query.get_or_404(Investor_ID)
    form = Create_Investor()
    if form.validate_on_submit():
        investor.FirstName = form.FirstName.data
        investor.LastName = form.LastName.data
        investor.email = form.Email.data
        db.session.commit()
        flash('Investor Information has been updated!', 'success')
        return redirect(url_for('investors.Investors', Investor_ID=investor.InvestorID))
    elif request.method == 'GET':
        form.FirstName.data = investor.FirstName
        form.LastName.data = investor.LastName
        form.Email.data = investor.email
    return render_template('Create_Investor.html', title='Update Investor Information',
                           form=form, legend='Update Investor Information')

@investors.route("/AddInvestment", methods=['GET','POST'])
@login_required
def AddInvestment():
    # Add a new investment.
    form = Add_Investment()
    funds = Fund.query.all()
    investor = Investor.query.all()
    inv_value = Fund.query.filter_by(FundID = form.Fund_ID.data).first()
    if form.validate_on_submit():
        investment = Investment(Fund_ID = form.Fund_ID.data,
                                Investor_ID = form.Investor_ID.data,
                                Units = form.Units.data, 
                                Investment_Value = inv_value.UnitPrice * form.Units.data
                                )
        db.session.add(investment)
        db.session.commit()
        flash('Investment Added.', 'success')
        return redirect(url_for('investors.Investors'))
    return render_template('AddInvestment.html', title='Add a new Investment', form=form, funds = funds, investors=investor)