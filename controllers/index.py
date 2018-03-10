from flask import render_template, Blueprint, flash
from models.forms import EmailPasswordForm, RegisterForm

index = Blueprint("index", __name__)

FLASH_LEVEL = {
    "success": "success",
    "info": "info",
    "warning": "warning",
    "danger": "danger"
}


@index.route("/", methods=["GET", "POST"])
def welcome():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        flash({
            "message": "Login Successful",
            "level": FLASH_LEVEL["success"]
        })
        # add redirection logic

    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return render_template("index.html", form=form)


@index.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        flash({
            "message": "Login Successful",
            "level": FLASH_LEVEL["success"]
        })
        # add redirection logic
    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return render_template("signup.html", form=form)
