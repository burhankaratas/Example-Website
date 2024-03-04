from flask import Flask,render_template,flash,redirect,url_for,session,request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from flask_mail import Mail, Message
from functools import wraps
import random
import string
import datetime
from datetime import datetime


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "hokuveay"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

app.secret_key = "wp+6#vfg0y3zg^ybi1u=yr)iny5seqf1$ofrtudy#7(hg5u!%2-4jv3"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)