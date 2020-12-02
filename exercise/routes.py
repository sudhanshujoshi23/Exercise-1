from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from exercise import app, db
from exercise.forms import LoginForm, Create_Fund, Create_Investor
from exercise.models import Fund, Investment, Investor


@app.route("/")
def Home():
    return render_template('Home.html', title='Welcome')


@app.route("/Login", methods=['GET','POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You are now logged in.', 'success')
        return redirect(url_for('Home'))
    return render_template('Login.html', title='Login', form=form)



@app.route("/Funds", methods=['GET'])
def Funds():
    Funds = Fund.query.all()
    return render_template('Funds.html', title="List of Funds", funds=Funds) 



@app.route("/Fund/New", methods=['GET','POST'])
def create_fund():
    form = Create_Fund()
    if form.validate_on_submit():
        fund = Fund(FundName = form.FundName.data, UnitPrice = form.UnitPrice.data)
        db.session.add(fund)
        db.session.commit()
        flash('Fund created in the Database.', 'success')
        return redirect(url_for('Funds'))
    return render_template('Create_Fund.html', title='Add new fund', form=form, legend='Add New Fund')

@app.route("/Fund/<int:Fund_ID>/update", methods=['GET','POST'])
def update_fund(Fund_ID):
    fund = Fund.query.get_or_404(Fund_ID)
    form = Create_Fund()
    if form.validate_on_submit():
        fund.FundName = form.FundName.data
        fund.UnitPrice = form.UnitPrice.data
        db.session.commit()
        flash('The fund has been updated!', 'success')
        return redirect(url_for('Funds', Fund_ID=fund.FundID))
    elif request.method == 'GET':
        form.FundName.data = fund.FundName
        form.UnitPrice.data = fund.UnitPrice
    return render_template('Create_Fund.html', title='Update Fund',
                           form=form, legend='Update Fund')

 


@app.route("/Investors", methods=['GET','POST'])
def Investors():
    Investors = Investor.query.all()
    return render_template('Investors.html', title="List of Investors", investors=Investors) 

@app.route("/Investor/New", methods=['GET','POST'])
def create_investor():
    form = Create_Investor()
    if form.validate_on_submit():
        investor = Investor(FirstName = form.FirstName.data, LastName = form.LastName.data, email = form.Email.data)
        db.session.add(investor)
        db.session.commit()
        flash('Investor created in the Database.', 'success')
        return redirect(url_for('Investors'))
    return render_template('Create_Investor.html', title='Add a new Investor', form=form)

@app.route("/Investor/<int:Investor_ID>/update", methods=['GET','POST'])
def update_investor(Investor_ID):
    investor = Investor.query.get_or_404(Investor_ID)
    form = Create_Investor()
    if form.validate_on_submit():
        investor.FirstName = form.FirstName.data
        investor.LastName = form.LastName.data
        investor.email = form.Email.data
        db.session.commit()
        flash('Investor Information has been updated!', 'success')
        return redirect(url_for('Investors', Investor_ID=investor.InvestorID))
    elif request.method == 'GET':
        form.FirstName.data = investor.FirstName
        form.LastName.data = investor.LastName
        form.Email.data = investor.email
    return render_template('Create_Investor.html', title='Update Investor Information',
                           form=form, legend='Update Investor Information')




  

