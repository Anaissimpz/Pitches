from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):

    comment = TextAreaField('Pitch comment', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitchForm(FlaskForm):
    category = SelectField('category', choices=[('pickup-lines','pickup-lines'),('Interview-pitch','Interview-pitch'), ('Promotion-pitch', 'Promotion-pitch')])
    content= TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')