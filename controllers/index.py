from flask import render_template, Blueprint

index = Blueprint("index", __name__)

@index.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")
