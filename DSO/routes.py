from flask import Flask, render_template, url_for, flash, redirect, request
from DSO import app, db
from DSO.models import User
from flask_login import login_user, current_user, logout_user, login_required



# User Loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
with app.app_context():
    db.create_all()
    

@app.route("/login", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    # For simplicity, we'll just pass the path to the templates directory
    # In a real app, you'd want a more secure and robust way to handle file paths
    import os
    files = os.listdir('templates')
    print(files)
    return render_template('dashboard.html', files=files)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
