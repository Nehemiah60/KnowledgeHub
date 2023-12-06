from flask import Flask, render_template, url_for, request, redirect, flash
from fileinput import filename
from models import *
from forms import *
import os
import secrets
from PIL import Image


@app.route('/')
def index():
    return render_template('index.html')

#Register User
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form  = RegisterStudent(request.form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(    username      = form.username.data,
                        email         = form.email.data,
                        user_password = hashed_password
                    )
        try:
            db.session.add(user)
            db.session.commit()    
            flash(f'Account created for {form.username.data}!', 'success')  
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('student_list')) 
    return render_template('register.html', form=form)

#user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    #Lets first check if the current user is already logged in, and redirect them to there profile page
    form = LoginForm(request.form)
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.user_password, form.password.data):
                login_user(user)
                flash('Login successful', 'success')
                return redirect(url_for('user_profile')) 
            else:
                flash('Login attempt failed, check email and password', 'danger')
        except:
            flash('Unexpected error occured')
    return render_template('login.html', form=form)

#user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#Function to save a picture image in our db
def save_profpic(form_picture):
    random_hex      = secrets.token_hex(8)
    f_name, f_ext   = os.path.splitext(form_picture.filename)
    picture_fn      = random_hex + f_ext
    picture_path    = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size     = (150,150)  
    my_image        = Image.open(form_picture)
    my_image.thumbnail(output_size)
    my_image.save(picture_path)

    return picture_fn
    
#user profile
@app.route('/profile', methods=["GET", "POST"])
@login_required
def user_profile():
    form = ProfileUpdateForm()
    image_file = url_for('static', filename='images/' + current_user.image_file)
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_profpic(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email    = form.email.data
        db.session.commit()
        flash('Your details are updated successfully', 'success')
        return redirect(url_for('user_profile'))

    return render_template('profile.html', form=form, image_file=image_file)

#courses page
@app.route('/courses', methods=['POST', 'GET']) 
@login_required
def courses():
    image_file  = url_for('static', filename='images/' + current_user.image_file)
    form=EnrollUserForm()
    courses = Course.query.all()
    return render_template('courses.html',  courses=courses, form=form, image_file=image_file)

@app.route('/course_details/<int:course_id>' , methods=['POST', 'GET'])
@login_required
def course_details(course_id):
    image_file  = url_for('static', filename='images/' + current_user.image_file)
    user_id     = current_user.id
    module_id   = Module.query.filter_by(course_id=course_id)
    module_progress= {}

    # for module in modules
    
    return render_template('course_details.html', image_file=image_file)

#modules page
@app.route('/intro-module', methods=['POST', 'GET'])
@login_required
def modules():
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('intro-module.html', image_file=image_file)


#Enroll User to a Course
@app.route('/enroll-user/<int:course_id>', methods=['POST','GET'])
@login_required
def enroll_user(course_id):
    form = EnrollUserForm(request.form)
    user = current_user
    course = Course.query.get_or_404(course_id=id)

    #Check if the user is already enrolled in the course
    if course in user.courses:
        flash('You are already enrolled in this course', 'danger')
        return redirect(url_for('courses'))

    db.session.execute(
        enrollment.insert().values(
            user_id=user.id,
            course_id=course.id,
            username=user.username,
            course_title=course.title
        )
    )
    db.session.commit()
    return render_template('courses.html', form=form)


#introduction module
@app.route('/about-program', methods=['POST', 'GET'])
@login_required
def about_program():
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('about_program.html', image_file=image_file)
    
#program duration
@app.route('/duration', methods=['POST', 'GET']) 
@login_required
def program_duration():
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('program-duration.html', image_file=image_file)

@app.route('/join-community', methods=['POST', 'GET'])
@login_required
def join_community():
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('join-community.html', image_file=image_file)

#FUNCTION TO SEND A RESET PASSWORD LINK TO MY EMAIL
def password_request_email(user):
    token = user.generate_token()
    email_message = Message('Password Reset Request', 
                            sender='knowledgehub@gmail.com', 
                            recipients=[user.email])
    email_message.body = f'''Visit the link to reset your password:
{url_for('reset_password_form', token=token, _external=True)}

If you did not make this request, Kindly ignore the email. 
    
    '''
    mail.send(email_message)

#RESET PASSWORD ROUTE
@app.route('/reset_password_link', methods=['POST', 'GET'])
def reset_request():
    #ensure the user is logged out before resseting their password
    if current_user.is_authenticated:
        return redirect(url_for('user_profile'))
    form = RequestLinkForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password_request_email(user)
        flash('Email has been sent with the instructions to reset password')
        return redirect(url_for('login'))
    return render_template('request_password_reset.html', title='Reset Password', form=form)

#A ROUTE TO RESET THE PASSWORD ONCE THE LINK IS CLICKED
@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_password_form(token):
    if current_user.is_authenticated:
        return redirect(url_for('user_profile'))
    user = User.validate_token(token)
    if user is None:
        flash('The token has expired', 'danger')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password     = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.user_password = hashed_password
        db.session.commit()
        flash('Your password has been changed. You are able to Log in with New Password', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form, token=token)
    

#Add student
@app.route('/students/add', methods=['GET','POST'])
def add_student():
    form        = StudentForm(request.form)
    if form.validate() and 'image' in request.files:
        student = Students(
            first_name  = form.first_name.data,
            second_name = form.second_name.data,
            email       = form.email.data,
            fee_paid    = form.fee_paid.data
        )
        image           = request.files['image']
        if image:
            try:
                filename    = image.filename
                image.save(os.path.join('static/images', filename))
                student.image = f'static/images/{filename}'
                db.session.add(student)
                db.session.commit()
            except:
                db.session.rollback()
            finally:
                db.session.close()
            return redirect(url_for('student_list'))
    return render_template('add_student_form.html', form=form)

#List of students
@app.route('/students')
def student_list():
    form    = StudentForm(request.form)
    student = Students.query.all()
    return render_template('add_student_form.html', student=student, form=form)

#Student Details
@app.route('/students/<int:id>')
def student_detail(id):
    student   = db.session.query(Students, Fees).join(Fees, Students.id==Fees.id).filter(Students.id==id).all()
    return render_template('student_detail.html', student=student)

#Update Students
@app.route('/students/<int:id>/update', methods=['GET','POST'])
def update_student(id):
    form = StudentForm(request.form)
    student = Students.query.get_or_404(id)
    if form.validate() and 'image' in request.files:
        student.first_name  = form.first_name.data,
        student.second_name = form.second_name.data,
        student.email       = form.email.data,
        student.fee_paid    += form.fee_paid.data
        student.image       =  request.files['image']

        image  = request.files['image']

        if image:
            try: 
                filename    = image.filename
                image.save(os.path.join('static/images', filename))
                student.image = f'images/{filename}'
                db.session.commit()
            except:
                db.session.rollback()
            finally:
                db.session.close()
            return redirect(url_for('student_list'))
    return render_template('update_student.html',student=student, form=form)

#Delete Students
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
        try:
            student = Students.query.get_or_404(id)
            db.session.delete(student)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('student_list'))
    
#Error handler
@app.errorhandler(401)
def unauthorized(error):
    flash('You Must be Logged in to Access the Page.', 'danger')
    return redirect(url_for('login'))
 


if __name__ == '__main__':
    app.run(debug=True)

