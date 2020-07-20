# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session

# import requests #To access our API

from jeopardy import Jeopardy

player = Jeopardy("")
# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Anoopa"
    return render_template('index.html')

@app.route("/random", methods=["GET", "POST"])
def jeopardy_random():
    # Use jservice "/api/random" to get 1 jeopardy clue
    if request.method == "GET":
        return "Go back to home"
    elif request.method == "POST":
        data = request.form
        if player.name == "":
            player.name = data["name"]
            return render_template("random_clue.html", data={})
        else:    
            return render_template("random_clue.html", data=data)
    else:
        return "idk what happened"