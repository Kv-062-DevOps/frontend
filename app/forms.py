from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    second_name = StringField('Last name',
                           validators=[DataRequired(), Length(min=2, max=20), ])
    types = SelectField('Position',
                           choices=[('manager', 'manager'), ('designer', 'designer'), ('developer', 'developer')])
    default_salary = DecimalField('Salary',
                           validators=[DataRequired()])
    experience = DecimalField('Experience',
                           validators=[DataRequired()])
    submit = SubmitField('Save')
