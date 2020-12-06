from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class Create_Investor(FlaskForm):
    # Flask Form for creating a new Investor.
    FirstName = StringField('FirstName', validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('LastName', validators=[DataRequired(), Length(min=2, max=20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

class Add_Investment(FlaskForm):
    # Flask Form for creating a new investment.
    Fund_ID = IntegerField('Fund', validators=[DataRequired()])
    Investor_ID = IntegerField('Investor', validators=[DataRequired()])
    Units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField('Add Investment')

