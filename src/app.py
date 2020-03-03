__author__ = 'jrReubin'

from flask import Flask, render_template, request, session
from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key = "james"


@app.route('/')
def hello_method():
    print("back to here")
    return render_template('login.html')

@app.before_first_request
def intialize_db():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email']=None

    return render_template("profile.html", email=session['email'])

@app.route('/register', methods=['POSTS'])

if __name__ == '__main__':
    app.run(port=4995)
