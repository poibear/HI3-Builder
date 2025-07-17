#TODO migrate to fastapi/react
import os
import math
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for, flash, jsonify

app = Flask(__name__, template_folder="templates")

@app.context_processor 
def datetime_variable(): # for copyright date
    return {"datetime": datetime}

@app.route("/")
def index():
    # request for prediction
    if len(request.query_string.decode("utf-8").split("&")) == 5:
        details = jsonify(request.args.to_dict())
        print(details)
    return render_template("index.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.config["TEMPLATES_AUTO_RELOAD"] = True # reload on html change
    app.secret_key = 'supa secretz'
    app.debug = True
    
    app.run(host=host, port=port)