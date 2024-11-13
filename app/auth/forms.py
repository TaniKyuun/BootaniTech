from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Optional, ValidationError, DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    firstname = StringField(
        ("First Name"),
        validators=[DataRequired()],
    )
    lastname = StringField(
        ("Last Name"),
        validators=[DataRequired()],
    )
    email = StringField(
        ("Email"),
        validators=[
            DataRequired(),
        ],
    )
    password = PasswordField(("Password"), validators=[DataRequired()])
    password2 = PasswordField(
        ("Repeat Password"), validators=[DataRequired(), EqualTo("password")]
    )
    in_company = BooleanField(("Are you registering as a company?"))
    company_name = StringField(
        ("Company Name"),
    )

    def validate_company_name(self, company_name):
        if self.in_company.data and not company_name.data:
            raise ValidationError(
                "Company Name is required when In Company is checked."
            )

    submit = SubmitField(("Register"))
