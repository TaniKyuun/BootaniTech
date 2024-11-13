import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from app import db
from app.auth.forms import LoginForm, RegistrationForm
from app.models import user_credentials

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(user_credentials).where(
                user_credentials.user_email == form.email.data
            )
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        if not form.in_company.data:
            form.company_name.data = None
        user = user_credentials(
            user_firstname=form.firstname.data,
            user_lastname=form.lastname.data,
            user_email=form.email.data,
            user_in_company=form.in_company.data,
            user_company=form.company_name.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(("Congratulations, you are now a registered user!"))
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title=("Register"), form=form)
