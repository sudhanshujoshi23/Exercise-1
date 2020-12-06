from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class Create_Fund(FlaskForm):
    # Flask Form for Creating a Fund.
    FundName = StringField('FundName', validators=[DataRequired(), Length(min=5, max=50)])
    UnitPrice = FloatField('UnitPrice', validators=[DataRequired()])
    submit = SubmitField('Submit')