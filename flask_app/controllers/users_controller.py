# only purpose of the controller is to connect to routes
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User
from flask_app.models.dealz_model import Dealz
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
from flask import flash


# Login page - VIEW
@app.route("/")
def index():
    return render_template("homepage.html")


# Registering - method - action
@app.route("/users/register", methods=["POST"])
def register():
    result = User.to_validate(request.form)
    if not result:
        return redirect("/")

    # 1st thing we do is hash the entered password
    new_password = bcrypt.generate_password_hash(request.form["password"])
    user_data = {
        **request.form,
        "password": new_password,
    }
    user_id = User.create(user_data)
    session["user_id"] = user_id
    return redirect("/homepage")


@app.route("/homepage")
def home():
    # Creating a ROUTE GUARD - that allows to check if the key is in session, and if not, a user cannot manually visit this page
    if "user_id" not in session:
        return redirect("/")
    # Storing the user's id to render to the HTML page
    logged_user = User.get_by_id(session["user_id"])
    # Getting all of the dealz to show
    all_dealz = Dealz.get_all()
    return render_template("welcome.html", logged_user=logged_user, all_dealz=all_dealz)


# This is the log out route
@app.route("/logout")
def logout():
    # Clears session when logging out
    session.clear()
    return redirect("/")


#  This is the log in route - action / post
@app.route("/users/login", methods=["POST"])
def login():
    registered_user = User.get_by_email(request.form["email"])

    # if the email is not in the database, flash the following message
    if not registered_user:
        flash("No history was found in our records.")
        return redirect("/")
    if not bcrypt.check_password_hash(
        registered_user.password, request.form["password"]
    ):
        flash("Invalid credentials.")
        return redirect("/")
    session["user_id"] = registered_user.id

    return redirect("/homepage")
