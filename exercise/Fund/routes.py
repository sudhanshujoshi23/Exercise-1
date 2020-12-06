from flask import render_template, url_for, flash, redirect, request, Blueprint
from exercise import db
from exercise.Fund.forms import Create_Fund
from exercise.models import Fund, Users
from flask_login import login_required, current_user 


funds = Blueprint('funds', __name__)


@funds.route("/Funds", methods=['GET'])
@login_required
def Funds():
    # List of all the funds.
    Funds = Fund.query.all()
    return render_template('Funds.html', title="List of Funds", funds=Funds) 



@funds.route("/Fund/New", methods=['GET','POST'])
@login_required
def create_fund():
    # Create a new fund.
    form = Create_Fund()
    
    if form.validate_on_submit():
        fund = Fund(FundName = form.FundName.data, UnitPrice = form.UnitPrice.data)
        db.session.add(fund)
        db.session.commit()
        flash('Fund created in the Database.', 'success')
        return redirect(url_for('funds.Funds'))
    return render_template('Create_Fund.html', title='Add new fund', form=form, legend='Add New Fund')

@funds.route("/Fund/<int:Fund_ID>/update", methods=['GET','POST'])
@login_required
def update_fund(Fund_ID):
    # Update an existing fund.
    fund = Fund.query.get_or_404(Fund_ID)
    form = Create_Fund()
    if form.validate_on_submit():
        fund.FundName = form.FundName.data
        fund.UnitPrice = form.UnitPrice.data
        db.session.commit()
        flash('The fund has been updated!', 'success')
        return redirect(url_for('funds.Funds', Fund_ID=fund.FundID))
    elif request.method == 'GET':
        form.FundName.data = fund.FundName
        form.UnitPrice.data = fund.UnitPrice
    return render_template('Create_Fund.html', title='Update Fund',
                           form=form, legend='Update Fund')