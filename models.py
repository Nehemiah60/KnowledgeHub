from config import *

#Used to load a user with their specific id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Students(db.Model):
    __tablename__ = "students"
    id          = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String(100), unique=True, index=True)
    second_name = db.Column(db.String(100), unique=False, index=True)
    email       = db.Column(db.String(100), unique=True, index=True)
    image       = db.Column(db.String(), nullable=True)
    fee_paid    = db.Column(db.Integer, nullable=False)
   
    def __repr__(self):
        return f"Students('{self.first_name}', '{self.second_name}', '{self.email}') "
    
class Fees(db.Model):
    __tablename__ = "fees"
    id          = db.Column(db.Integer, primary_key=True)
    fee_total   = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Fees ('{self.fee_total}')"
        
enrollment = db.Table(
            'enrollment',
            db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
            db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
            db.Column('username', db.String(100)),
            db.Column('course_title', db.String())

            )
    

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(100), index=True, unique=True)
    email         = db.Column(db.String(100), index=True, unique=True)
    image_file    = db.Column(db.String(100), nullable=False, default='default.jpg')
    user_password = db.Column(db.String(100))
    joined_date   = db.Column(db.DateTime, default=datetime.utcnow)
    courses       = db.relationship('Course', secondary=enrollment, backref='users')

    def generate_token(self, expire_timestamp=3600):
        payload = {'user_id': self.id, 
                   'exp': datetime.utcnow() + timedelta(seconds=expire_timestamp)}

        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm= 'HS256')

    @staticmethod
    def validate_token(token):
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['user_id']
            return User.query.get(user_id)
        except jwt.ExpiredSignatureError:
            return 'Token has expired'
        except (jwt.InvalidTokenError, KeyError):
            return 'Token is invalid'

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Course(db.Model):
    __tablename__ = 'course'
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(100), nullable=False)
    description   = db.Column(db.Text, nullable=False)
    enrolled_user = db.Column(db.Integer)

    def __repr__(self):
        return f"Course('{self.title}', '{self.description}')"


class Module(db.Model):
    __tablename__ = 'module'
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(100), nullable=False)
    course_id     = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f"Module('{self.title}')"
   
class UserProgress(db.Model):
    id                      = db.Column(db.Integer, primary_key=True)
    user_id                 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id               = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    module_id               = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    progress_percentage     = db.Column(db.Float, default=0.0)




    
    
    
    
    
    



    