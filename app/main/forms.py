from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):

    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    body = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')


class SubscriptionForm(FlaskForm):

    email = StringField('Email Address', validators=[Required()])
    submit = SubmitField('Subscribe')
