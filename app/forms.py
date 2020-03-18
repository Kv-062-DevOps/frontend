from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    firstname = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    position = StringField('Position',
                           validators=[DataRequired(), Length(min=2, max=20)])
    salary = DecimalField('Salary',
                           validators=[DataRequired()])
    experiance = DecimalField('Experiance',
                           validators=[DataRequired()])
    submit = SubmitField('Save')
