import os

from cs50 import SQL
from math import trunc
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///reg.db")

@app.route("/")
@login_required
def index():
    username = session["username"]
    contact = session["contact"]
    return render_template("index.html", username=username, contact=contact)

@app.route("/main", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        return redirect("/register")
    if request.method == "GET":
        return render_template("main.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any session data
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        username = request.form.get("username")
        contact = request.form.get("contact")
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["username"] = username
        session["contact"] = rows[0]["contact"]
        session["user_id"] = rows[0]["user_id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":

        #Error checking
        if request.form.get("password") != request.form.get("passwordconf"):
            return apology("Passwords do not match", 403)
        username = request.form.get("username")
        if not username:
            return apology("Username cannot be empty")
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(rows) != 0:
            return apology("Username already taken")

        hashpass = generate_password_hash(request.form.get("password"))
        contact = request.form.get("contact")
        db.execute("INSERT INTO users (username, password, contact) VALUES (?,?,?)", username, hashpass, contact)

        return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
