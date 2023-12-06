import os
from flask import Flask
import jwt
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from datetime import datetime
from flask_login import (UserMixin, LoginManager, login_user, 
                            current_user, logout_user, login_required)
from flask_bcrypt import Bcrypt  #Used for hashing password
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nehecode@localhost:5432/yolo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ywngitnotw@!'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']= os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']= os.environ.get('EMAIL_PASS')
mail = Mail(app)

db  = SQLAlchemy(app)
bcrypt = Bcrypt(app) # Create a bcrpt object for or app
login_manager = LoginManager(app)
migrate = Migrate(app,db)

