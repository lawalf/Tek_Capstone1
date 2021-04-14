from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Tractor:')
    submit = SubmitField('Add Tractor')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Tractor to Remove:')
    submit = SubmitField('Remove Tractor')
