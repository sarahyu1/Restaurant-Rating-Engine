from flask import Flask, redirect, render_template, request, url_for
#import pandas as pd
#from dbconnect import connection
#from wtforms import Form, BooleanField, TextField, PasswordField, validators
#from passlib.hash import sha256_crypt


app = Flask(__name__)
comments = []
feature_list=[]
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":

        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    feature_list.append(request.form["Takes Reservations"])
    return redirect(url_for('index'))

