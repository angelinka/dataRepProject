# Server file

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from collegeDAO import collegeDAO

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# Define flask app and session secret key
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.secret_key = '4yiYAJa6sJe1xBw8UPHtq4oAAz0ynFCg'

#mysql = MySQL(app)

@app.route('/')
# Login route
# Code adapted from https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		data = [
      		email, password
      		
		]
		#app.logger.info('got IDs')
		account = collegeDAO.verify(data)
		#app.logger.info('veryfied')
		if account:
			session['loggedin'] = True
			session['id'] = account['studentID']
			session['username'] = account['firstname']
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
			#return redirect(url_for('index',name = session['username']))
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	app.logger.info('in register')
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'firstname'  in request.form and 'lastname'  in request.form:
		app.logger.info('first if')
		email = request.form['email']
		password = request.form['password']
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		gender = request.form.get('gender', '')
		dob = request.form['dob']
		check = [email]
		account = collegeDAO.checkEmail(check)
		if account:
			msg = 'Account already exists!'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address!'
		#elif not re.match(r'[A-Za-z]+', firstname):
			#msg = 'First name must contain only characters!'
		#elif not re.match(r'[A-Za-z]+', lastname):
			#msg = 'Last name must contain only characters!'
		elif not password or not email or not firstname or not lastname or not gender or not dob:
			msg = 'Please fill out all the fields!'
		else:
			data = [email, password, firstname, lastname, gender, dob]
			app.logger.info('passing details')
			account = collegeDAO.createStudent(data)
			msg = 'You have successfully registered!'
			render_template('register.html', msg = msg)
			#return redirect(url_for('login'), msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form!'
		
	return render_template('register.html', msg = msg)

if __name__ == "__main__":
    app.run(debug=True)