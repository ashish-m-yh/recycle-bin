from flask import render_template, Blueprint, flash, redirect, url_for
from models.forms import EmailPasswordForm, RegisterForm, ResetPasswordForm
from models.org import Organization
from server import login_manager
from flask_login import current_user, login_user, logout_user, login_required

index = Blueprint("index", __name__)

FLASH_LEVEL = {
    "success": "success",
    "info": "info",
    "warning": "warning",
    "danger": "danger"
}


@login_manager.user_loader
def load_user(user_id):
    return Organization.get(user_id)


@index.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.welcome'))


@index.route('/reset_password', methods=["POST"])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        data = form.data

        user = Organization.get_by_email(data["email"])

        if user:
            user.set_password(data["password"])
            user.update()
            flash({
                "message": "Password reset successfully.",
                "level": FLASH_LEVEL["success"]
            })
        else:
            flash({
                "message": "Invalid email address entered. Please try again.",
                "level": FLASH_LEVEL["danger"]
            })

    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return redirect(url_for('index.welcome'))


@index.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")


@index.route("/", methods=["GET", "POST"])
def welcome():
    if current_user.is_authenticated:
        return redirect(url_for("index.dashboard"))

    form = EmailPasswordForm()
    reset_password_form = ResetPasswordForm()
    if form.validate_on_submit():
        data = form.data
        user = Organization.login(data["email"], data["password"])
        if user:
            login_user(user, remember=False)
            flash({
                "message": "Login Successful",
                "level": FLASH_LEVEL["success"]
            })
            return redirect(url_for("index.dashboard"))
        else:
            flash({
                "message": "Invalid Username/Password",
                "level": FLASH_LEVEL["danger"]
            })

    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return render_template("index.html", form=form, reset_password_form=reset_password_form)


@index.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data

        user_already_exists = Organization.get_by_email(data["email"])
        if user_already_exists:
            flash({
                "message": "User already exists.",
                "level": FLASH_LEVEL["warning"]
            })
            return render_template("signup.html", form=form)

        organization = Organization()
        organization.set_password(data["password"])
        organization.email = data["email"]
        organization.address = data["address"]
        organization.contact_no1 = data["contact1"]
        organization.contact_no2 = data["contact1"] if data["contact1"] else None
        organization.contact_person = data["contact_person"]
        organization.industry_id = int(data["industry"])
        organization.org_name = data["name"]

        waste_gen_list = map(lambda x: x.split("::"), data["waste_generated_list"].split("||"))
        waste_gen_list = filter(lambda x: len(x) > 1, waste_gen_list)
        waste_req_list = map(lambda x: x.split("::"), data["waste_required_list"].split("||"))
        waste_req_list = filter(lambda x: len(x) > 1, waste_req_list)

        try:
            organization.save(organization, waste_req_list, waste_gen_list)
            flash({
                "message": "Registration Successful!",
                "level": FLASH_LEVEL["success"]
            })
            return redirect(url_for("welcome"))

        except Exception as e:
            print("Error while saving: " + str(e))
            flash({
                "message": "Unable to create user. Please try again later.",
                "level": FLASH_LEVEL["danger"]
            })

    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return render_template("signup.html", form=form)
