from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, Email, Optional, EqualTo
from wtforms.fields.html5 import TelField
from industry import Industry
from waste import Waste
from states import State
from district import District
from place import Place

ALL_INDUSTRIES = Industry.get_all_industry()
ALL_WASTES = Waste.get_all_waste()
ALL_STATES = State.get_all_states()
ALL_DISTRICTS = District.get_all_district()
ALL_PLACES = Place.get_all_places()


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class RegisterForm(FlaskForm):
    industry = SelectField('Industry', choices=map(lambda x: (str(x.id), x.industry), ALL_INDUSTRIES))
    name = StringField('Oragnization Name', validators=[DataRequired()])
    contact1 = TelField('Contact Number 1')
    contact2 = TelField('Contact Number 2')
    address = StringField('Address', validators=[DataRequired()])
    contact_person = StringField('Contact Person', validators=[DataRequired()])
    waste_generated = SelectMultipleField("Waste Generated",
                                          choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                      ALL_WASTES), validators=[Optional()])
    waste_required = SelectMultipleField("Waste Required",
                                         choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                     ALL_WASTES), validators=[Optional()])

    waste_required_list = HiddenField("WasteRequiredList")
    waste_generated_list = HiddenField("WasteRequiredList")

    state = SelectField('State', choices=map(lambda x: (str(x.id), x.name), ALL_STATES))
    district = SelectField('District',
                           choices=[('-', 'Select District (optional)')] + map(lambda x: (str(x.id), x.name),
                                                                               ALL_DISTRICTS))
    place = SelectField('Place',
                        choices=[('-', 'Select Place (optional)')] + map(lambda x: (str(x.id), x.name), ALL_PLACES))

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class EditProfileForm(FlaskForm):
    email = StringField('Email', render_kw={'readonly': True})
    industry = SelectField('Industry', choices=map(lambda x: (str(x.id), x.industry), ALL_INDUSTRIES))
    name = StringField('Oragnization Name', validators=[DataRequired()])
    contact1 = TelField('Contact Number 1')
    contact2 = TelField('Contact Number 2')
    address = StringField('Address', validators=[DataRequired()])
    state = SelectField('State', choices=map(lambda x: (str(x.id), x.name), ALL_STATES))
    district = SelectField('District',
                           choices=[('-', 'Select District (optional)')] + map(lambda x: (str(x.id), x.name),
                                                                               ALL_DISTRICTS))
    place = SelectField('Place',
                        choices=[('-', 'Select Place (optional)')] + map(lambda x: (str(x.id), x.name), ALL_PLACES))
    contact_person = StringField('Contact Person', validators=[DataRequired()])


class EditWasteForm(FlaskForm):
    waste_generated = SelectMultipleField("Waste Generated",
                                          choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                      ALL_WASTES), validators=[Optional()])
    waste_required = SelectMultipleField("Waste Required",
                                         choices=map(lambda x: (str(x.waste_id), x.waste.title()),
                                                     ALL_WASTES), validators=[Optional()])

    waste_required_list = HiddenField("WasteRequiredList")
    waste_generated_list = HiddenField("WasteRequiredList")
