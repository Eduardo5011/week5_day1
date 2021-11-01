from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import User
import random
from jinja2 import Markup

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    r1=random.randint(1,100)
    r2=random.randint(100,200)
    r3=random.randint(200,300)
    r4=random.randint(300,400)

    r1_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r1}.png" style="height:75px">')
    r2_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r2}.png" style="height:75px">')
    r3_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r3}.png" style="height:75px">')
    r4_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r4}.png" style="height:75px">')

    icon = RadioField('Choose a pokemon', 
                    choices=[(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img)], 
                    validators=[DataRequired()])
    
      

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    r1=random.randint(1,100)
    r2=random.randint(100,200)
    r3=random.randint(200,300)
    r4=random.randint(300,400)

    r1_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r1}.png" style="height:75px">')
    r2_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r2}.png" style="height:75px">')
    r3_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r3}.png" style="height:75px">')
    r4_img=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{r4}.png" style="height:75px">')

    icon = RadioField('Choose a pokemon', 
                    choices=[(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img)], 
                    validators=[DataRequired()])
    
    


