from flask_wtf import FlaskForm
from wtforms.validators import Required
from ..models import User,Subscriber
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError


class SubscriberForm(FlaskForm):
    email = TextAreaField('enter your valid email address.',validators = [Required()])
    username = TextAreaField('username', validators = [Required()])
    submit = SubmitField('Submit')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email = data_field.data).first():
            raise ValidationError('Your data already exists')