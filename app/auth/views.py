"""Authentication views"""
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import LoginForm, RegistrationForm
from app.main.urls import auth
from app.models import User
from app import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """method to login user"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            flash("Invalid Username or password")
            return redirect(url_for('auth.login'))
        login_user(user, form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form, title="Login")


@auth.route('/register', methods=["GET", "POST"])
def register():
    """View route for registering a user"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title="Sign Up")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("main.index"))
