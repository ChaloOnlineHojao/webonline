from flask import Blueprint,render_template,redirect,session,request
import json
from models.userDbUtility import UserDbUtility
admin = Blueprint('admin', __name__)
usr = "admin"
@admin.route("/admin")
def admin_func():     
      if 'user' in session:
            return redirect('/admin/dashboard')
      return redirect('/admin/login')

@admin.route("/admin/dashboard")
def dashboard():
      if 'user' in session:
            allUsers = UserDbUtility.getAllUsers()
            return render_template("manageusers.html",allUsers=allUsers)
      return redirect("/admin/login")

@admin.route("/admin/user/changeStatus/<string:user>")
def changeStatus(user):
      if 'user' in session:
            oper = request.args.get('oper')
            if oper != None:
                  UserDbUtility.changeUserStatus(user,oper)
            return redirect("/admin/dashboard")
      return redirect("/admin/login")