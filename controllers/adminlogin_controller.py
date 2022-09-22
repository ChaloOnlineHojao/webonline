from flask import Blueprint,render_template,redirect,request,session
from models.loginDbUtility import LoginDbUtility
from models.userDbUtility import UserDbUtility
adminlogin = Blueprint('adminlogin', __name__)
@adminlogin.route("/admin/login")
def login():
      if 'user' in session:
            return redirect('/admin/dashboard')
      return render_template('adminlogin.html')

@adminlogin.route("/admin/loginsbt", methods=['GET','POST'])
def loginsbt():
      if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            status = LoginDbUtility.checkForUser(email,password) 
            if status == 1:
                  session['user']=email
                  return redirect("/admin/dashboard")
            else:
                  return redirect("/admin/login")

@adminlogin.route("/admin/logout")
def logout():
    session.pop('user')
    return redirect("/admin/login")
