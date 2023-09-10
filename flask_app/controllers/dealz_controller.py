# only purpose of the controller is to connect to routes
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User
from flask_app.models.dealz_model import Dealz
from flask import flash


# Rendering the sell page
@app.route("/new")
def new_sell():
    return render_template("car_sell.html")


# Creating a POST route to inject data into DB
@app.route("/sell/create", methods=["POST"])
def create_sell_post():
    if not Dealz.validate(request.form):
        return redirect("/new")
    Dealz.create(request.form)
    return redirect("/homepage")


# Display data per ID
@app.route("/new/<int:id>")
def display_one(id):
    dealz = Dealz.get_by_id(id)
    users = User.get_by_id(dealz.user_id)
    return render_template("dealz_show_one.html", dealz=dealz, user=users)


# Edit page
@app.route("/new/<int:id>/edit")
def edit(id):
    this_deal = Dealz.get_by_id(id)
    return render_template("edit_selling.html", this_deal=this_deal)


# Update route for user to make changes
@app.route("/new/update", methods=["POST"])
def update_deal():
    if not Dealz.validate(request.form):
        return redirect(f"/new/{request.form['id']}/edit")
    Dealz.update(request.form)
    return redirect("/homepage")


# Delete data from DB
@app.route("/new/<int:id>/delete")
def delete(id):
    data = {"id": id}
    Dealz.delete(data)
    return redirect("/homepage")
