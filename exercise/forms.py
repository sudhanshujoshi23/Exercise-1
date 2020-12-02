from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email

class Create_Fund(FlaskForm):
    FundName = StringField('FundName', validators=[DataRequired(), Length(min=5, max=50)])
    UnitPrice = FloatField('UnitPrice', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Create_Investor(FlaskForm):
    FirstName = StringField('FirstName', validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('LastName', validators=[DataRequired(), Length(min=2, max=20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
    
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')






