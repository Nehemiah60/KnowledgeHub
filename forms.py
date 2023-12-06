from flask import Flask
from flask_wtf import FlaskForm, Form
from wtforms import (StringField, SubmitField, IntegerField, 
                    FileField, PasswordField, DateTimeField, BooleanField)
from wtforms.validators import (DataRequired, Email, 
                                EqualTo, Length, ValidationError)
from flask_wtf.file import FileField, FileAllowed
from models import*

class StudentForm(FlaskForm):
    first_name    = StringField('First Name',  validators=[DataRequired(), Length(min=2, max=20)])
    second_name   = StringField('Second Name', validators=[DataRequired()])
    email         = StringField('Email Address', validators=[DataRequired()])
    image         = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png' ,'jpeg'])])
    fee_paid      = IntegerField('Fee Paid', default=0,validators=[DataRequired()])
    submit        = SubmitField()

class RegisterStudent(FlaskForm):
    username         = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    email            = StringField('Email', validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password do not match')])
    submit           = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("A user with that username already exists. Choose a different username")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("A user with that email already exists. Choose a different email")


class LoginForm(FlaskForm):
    email            = StringField('Email', validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired()])
    submit           = SubmitField('Login')

class ProfileUpdateForm(FlaskForm):
    username         = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    email            = StringField('Email', validators=[DataRequired(), Email()])
    picture          = FileField('Update Profile', validators=[FileAllowed(['png', 'jpg'], 'Only JPG and PNG File extensions are allowed!')] )
    submit           = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: # Ensure the username to be updated is not the same as the current username
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("A user with that username already exists. Choose a different username")

    def validate_email(self, email):
        if email.data != current_user.email: # Ensure the email to be updated is not equal to the same as current user email
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("A user with that email already exists. Choose a different email")


# Enroll User Form
class EnrollUserForm(FlaskForm):
    submit          = SubmitField('Enroll Today')

# ResetPasswordForm A link is sent to the email to reset password
class RequestLinkForm(FlaskForm):
    email           = StringField('Email', validators=[DataRequired(), Email()])
    submit          = SubmitField('Submit')

    #Validate whether there is a user with the provided mail
    def validate_email(self, email):
        user        = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no user with that email. Register first.')

class ResetPasswordForm(FlaskForm):
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password do not match')])
    submit           = SubmitField('Reset Password')
