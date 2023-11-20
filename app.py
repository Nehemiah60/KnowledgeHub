from flask import Flask, render_template, url_for, request, redirect, flash
from fileinput import filename
from models import *
from forms import *
import os
import secrets


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
    flash('You must be logged in to access the page.', 'danger')
    return redirect(url_for('login'))
 


if __name__ == '__main__':
    app.run(debug=True)

