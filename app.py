from flask import Flask, redirect, render_template
from controllers.adminlogin_controller import adminlogin
from controllers.admin_controller import admin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 
@app.route("/")
def home():
      return "Hello world by hemant"

@app.route("/server")
def server():
      return render_template('manageusers.html')

app.register_blueprint(adminlogin)
app.register_blueprint(admin)

app.run(debug=True)

