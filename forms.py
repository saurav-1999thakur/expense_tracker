from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange
from datetime import date

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=100)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class ExpenseForm(FlaskForm):
    description = StringField("Description", validators=[DataRequired(), Length(max=100)])
    amount = FloatField("Amount", validators=[DataRequired(), NumberRange(min=0.01, message="Amount must be greater than 0.01")])
    ch = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Other', 'Other')
    ]
    category = SelectField("Category", choices=ch, validators=[DataRequired()])
    # date = DateField("Expense Date", format="%y-%m-%d", default=date.today, validators=[DataRequired()])
    submit = SubmitField("Add Expense")