from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, Email, Optional, EqualTo
from wtforms.fields.html5 import TelField
from industry import Industry
from waste import Waste


class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ResetPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class RegisterForm(Form):
    all_industries = Industry.get_all_industry()
    all_wastes = Waste.get_all_waste()
    industry = SelectField('Industry', choices=map(lambda x: (str(x.id), x.industry), all_industries))
    name = StringField('Oragnization Name', validators=[DataRequired()])
    contact1 = TelField('Contact Number 1')
    contact2 = TelField('Contact Number 2')
    address = StringField('Address', validators=[DataRequired()])
    contact_person = StringField('Contact Person', validators=[DataRequired()])
    waste_generated = SelectMultipleField("Waste Generated",
                                          choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                      all_wastes), validators=[Optional()])
    waste_required = SelectMultipleField("Waste Required",
                                         choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                     all_wastes), validators=[Optional()])

    waste_required_list = HiddenField("WasteRequiredList")
    waste_generated_list = HiddenField("WasteRequiredList")

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
