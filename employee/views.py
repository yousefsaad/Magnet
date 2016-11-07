from Magnet import app, db
from flask import render_template, redirect, session, request, url_for, flash
from employee.form import RegisterForm, LoginForm
from employee.models import Employee
from employee.decorators import login_required, admin_required
import bcrypt


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        employee = Employee.query.filter_by(
        	live=True,
            username=form.username.data,
            ).first()
        if employee:
            if bcrypt.hashpw(form.password.data, employee.password) == employee.password:
                session['username'] = form.username.data
                session['is_admin'] = employee.is_admin
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect('index')
            else:
                error = "Incorrect password"
        else:
            error = "employee not found"
    return render_template('employee/login.html', form=form, error=error)

@app.route("/manageEmployees", methods=('GET', 'POST'))
#admin is required to fill the form in order to add a Receptionist
@admin_required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        fullname = form.fullname.data
        ssn = form.ssn.data
        email = form.email.data
        DOB = form.DOB.data
        job_title = form.job_title.data
        username = form.username.data
        password = hashed_password
        if job_title == 'Maneger' or job_title == 'maneger':
            is_admin = True
        else:
            is_admin = False
        live = False
        employee = Employee(fullname,ssn,email,DOB,job_title,username,password,is_admin,live)
        db.session.add(employee)
        db.session.commit()

        return redirect('/success')
    return render_template('manageEmployees.html', form=form)

##########################list of Active employees #####################
@app.route('/manageEmployees')
@login_required
@admin_required
def admin():
    #posts = Employee.query.order_by(Employee.id.desc())
    active = Employee.query.filter_by(live=True).order_by(Employee.id.desc())
    return render_template('manageEmployees.html', active=active)

@app.route('/success')
@login_required
def success():
    return "employee registered!"


@app.route('/manageEmployees/<int:employee_id>')
@admin_required
def delete(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first_or_404()
    employee.live = False
    db.session.commit()
    flash("Employee deleted")
    return redirect('/manageEmployees')



############################### Deactivated Employeees ################
@app.route('/inactiveEmployee')
@login_required
@admin_required
def inactive():
    #posts = Employee.query.order_by(Employee.id.desc())
    inactive = Employee.query.filter_by(live=False).order_by(Employee.id.desc())
    return render_template('inactiveEmployee.html', inactive=inactive)

@app.route('/inactiveEmployee/<int:employee_id>')
@admin_required
def reactivate(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first_or_404()
    employee.live = True
    db.session.commit()
    flash("Employee Activated")
    return redirect('/inactiveEmployee')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))

