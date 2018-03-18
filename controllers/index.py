from flask import render_template, Blueprint, flash
from models.forms import EmailPasswordForm, RegisterForm
from models.org import Organization

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
        data = form.data
        organization = Organization()
        organization.passwd = data["password"]
        organization.email = data["email"]
        organization.address = data["address"]
        organization.contact_no1 = data["contact1"]
        organization.contact_no2 = data["contact1"] if data["contact1"] else None
        organization.contact_person = data["contact_person"]
        organization.industry_id = int(data["industry"])
        organization.org_name = data["name"]

        waste_gen_list = map(lambda x: x.split("::"), data["wasteGeneratedList"].split("||"))
        waste_gen_list = filter(lambda x: len(x) > 1, waste_gen_list)
        waste_req_list = map(lambda x: x.split("::"), data["wasteRequiredList"].split("||"))
        waste_req_list = filter(lambda x: len(x) > 1, waste_req_list)

        try:
            organization.save(organization, waste_req_list, waste_gen_list)
            flash({
                "message": "Registration Successful!",
                "level": FLASH_LEVEL["success"]
            })
        except Exception as e:
            print("Error while saving: " + str(e))
            flash({
                "message": "Unable to create user. Please try again later.",
                "level": FLASH_LEVEL["danger"]
            })
            # add redirection logic
    for error in form.errors:
        flash({
            "message": error + " - " + ",".join(form.errors[error]),
            "level": FLASH_LEVEL["danger"]
        })
    return render_template("signup.html", form=form)
