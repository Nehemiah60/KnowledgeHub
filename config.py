from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from datetime import datetime
from flask_login import (UserMixin, LoginManager, login_user, 
                            current_user, logout_user, login_required)
from flask_bcrypt import Bcrypt  #Used for hashing password

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nehecode@localhost:5432/yolo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ywngitnotw@!'
db  = SQLAlchemy(app)
bcrypt = Bcrypt(app) # Create a bcrpt object for or app
login_manager = LoginManager(app)
migrate = Migrate(app,db)