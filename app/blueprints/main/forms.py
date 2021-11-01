from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class PokeForm(FlaskForm):
    poke_info = StringField('Search for a pokemon', validators=[DataRequired()])
    submit = SubmitField('Submit')