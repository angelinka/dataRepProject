# Server file

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort
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


@app.route('/')
def index():
   if not 'username' in session:
      return redirect(url_for('login'))

   return render_template('index.html', title='Index', name = session['username'])
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
		account = collegeDAO.verify(data)
		#app.logger.info('veryfied')
		if account:
			session['loggedin'] = True
			session['id'] = account['studentID']
			session['username'] = account['firstname']
			msg = 'Logged in successfully !'
			#return render_template('index.html', msg = msg)
			return redirect(url_for('index', name = session['username']))
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

		elif not password or not email or not firstname or not lastname or not gender or not dob:
			msg = 'Please fill out all the fields!'
		else:
			data = [email, password, firstname, lastname, gender, dob]
			app.logger.info('passing details')
			account = collegeDAO.createStudent(data)
			msg = 'You have successfully registered!'
        			
	elif request.method == 'POST':
		msg = 'Please fill out the form!'	
	return render_template('register.html', msg = msg)

# get all modules route
# curl http://127.0.0.1:5000/modules
@app.route('/modules')
def getAllMod():
    if not 'username' in session:
        app.logger.info('Access not authorised')
        abort(401)
    app.logger.info('Get all modules')
    return jsonify(collegeDAO.getAllMod())

# create module, returns created module info
@app.route('/modules', methods=['POST'])
def createMod():
   if not 'username' in session:
        app.logger.info('Access not authorised')
        abort(401)
   if not request.json:
        app.logger.info('Request format not json')
        abort(400)
		
   module = {
      "moduleCode": request.json["moduleCode"],
       "moduleName": request.json["moduleName"],
       "location": request.json["location"],
       "credits": request.json["credits"]
    }
   app.logger.info('Created module %s', module)
   return jsonify(collegeDAO.createMod(module))

# find By modulecode route
@app.route('/modules/moduleCode')
def findModutById(moduleCode):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get module with moduleCode %s', moduleCode)
   return jsonify(collegeDAO.findModById(moduleCode))

# update module, returns updated module info
@app.route('/modules/<string:moduleCode>', methods=['PUT'])
def updateMod(moduleCode):
   app.logger.info('Updated module flask', moduleCode)
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   foundMod = collegeDAO.findModById(moduleCode)
   # print(foundMod)
   if foundMod == {}:
      app.logger.info('moduleCode %s not found', moduleCode)
      return jsonify({}), 404
   currentMod = foundMod
   if 'moduleName' in request.json:
      currentMod['moduleName'] = request.json['moduleName']
   if 'location' in request.json:
      currentMod['location'] = request.json['location']
   if 'credits' in request.json:
      currentMod['credits'] = request.json['credits']
   collegeDAO.updateMod(currentMod)
   app.logger.info('Updated module %s', currentMod)
   return jsonify(currentMod)

# delete module, returns True/False if delete was done
@app.route('/modules/<string:moduleCode>', methods=['DELETE'])
def deleteMod(moduleCode):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   # check if module exists
   foundMod = collegeDAO.findModById(moduleCode)
   app.logger.info('mod code found ', foundMod)
   if foundMod == {}:
      app.logger.info('moduleCode %s not found', moduleCode)
      return jsonify({"done": False}), 404
   try:
      collegeDAO.deleteMod(moduleCode)
      app.logger.info('Deleted module %s', foundMod)
      return jsonify({"done": True})
   except:
      app.logger.info('Cannot delete moduleCode %s', moduleCode)
      return jsonify({"done": False})

    


if __name__ == "__main__":
    app.run(debug=True)