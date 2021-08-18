from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, SelectField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email 

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),])
    password = PasswordField('Password', validators=[DataRequired(),])
    genre = SelectField('Genre', choices = [('Stations'), ('Ambient/Dub/Fourth World'), ('House/Techno/Jungle/Drum n Bass'), ('Jazz/World/Soundtrack'), ('Rock/Pop/Folk'), ('Metal/Noise/Experimental')])
    mood = SelectField('Mood', choices = [('Default Mood (You Can Change This Later)'),('Facial Recognition Mode'),('Morning Coffee'), ('Afternoon Walk'), ('Dinner with Friends'), ('Late Night'), ('Contemplative'), ('Driving in a Hurry'), ('Reading the News')])
    submit_button = SubmitField('Register')



class UserSigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),])
    password = PasswordField('Password', validators=[DataRequired(),])
    submit_button = SubmitField('Sign In')

class ChangeGenre(FlaskForm):
    genre = SelectField('Genre', choices = [('Update Default Station'), ('Ambient/Dub/Fourth World'), ('House/Techno/Jungle/Drum n Bass'), ('Jazz/World/Soundtrack'), ('Rock/Pop/Folk'), ('Metal/Noise/Experimental')])
    submit_button = SubmitField('Update')

class ChangeMood(FlaskForm):
    mood = SelectField('Mood', choices = [('Update Default Mood'), ('Facial Recognition Mode'), ('Morning Coffee'), ('Afternoon Walk'), ('Dinner with Friends'), ('Late Night'), ('Contemplative'), ('Driving in a Hurry'), ('Reading the News')])
    submit_button = SubmitField('Update')

class UploadMood(FlaskForm):
    submit_button = SubmitField('Upload Photo')