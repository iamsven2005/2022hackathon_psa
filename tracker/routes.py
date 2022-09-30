from tracker import app
from flask import render_template, redirect, url_for, flash, request
from tracker.models import User
from tracker.forms import RegisterForm, LoginForm
from tracker import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# routes to the account registration page
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # checks whether the username, email_address and password are valid
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
        # if this is True, then add the newly set user credentials to the newly created account
        db.session.add(user_to_create)
        db.session.commit()
        # redirects user to the market page after account is created
        return redirect(url_for('user_dashboard'))

    if form.errors != {}:
        # an error message/log to tell the user of an error in creating a user
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register_page.html', form=form)


# routes to the login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    # fetches credentials from the LoginForm() in form.py
    form = LoginForm()
    # authenticates the user with their username and password
    if form.validate_on_submit():
        # filters to the username, important to always include '.first()'
        attempted_user = User.query.filter_by(username=form.username.data).first()
        # if this condition is true, logs the user in, else display error message that login credentials does not match
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('user_dashboard'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login_page.html', form=form)


# route to logout page
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login_page"))


@app.route('/admin')
@login_required
def admin_page():
    id = current_user.id
    user_id = User.query.order_by(User.id).all()
    
    if id == 1:
        return render_template("admin_page.html", user_id=user_id)
    else:
        flash("Sorry you must be admin!", category="warning")
        return redirect(url_for('user_dashboard')) 

@app.route('/dashboard')
@login_required
def user_dashboard():
    return render_template("user_dashboard.html")
