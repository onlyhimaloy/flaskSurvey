from lowusage import form


from flask_wtf import FlaskForm
from wtforms import  RadioField,TextAreaField, SubmitField, validators, StringField
from wtforms.validators import InputRequired, DataRequired


class SurvForm(FlaskForm):
    ans1 = RadioField('Please answer if you would like to Return the Server below', 
                       choices = [('1', 'Yes'), ('2', 'No'), ('3', 'Unknown Server')],validators=[DataRequired()])
    ans2 = TextAreaField('Reason or Comments',
                          validators=[DataRequired()],
                          render_kw = {
                             "placeholder": "Example 1. For the backup server, HA purpose etc",
                          })

    submit = SubmitField('Submit')



