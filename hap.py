from flask import Flask, render_template, request
import random
import csv
import hashlib
app = Flask(__name__)


@app.route("/")
def login():
    print request.headers          #only works for POST
    return render_template( 'login.html' )

@app.route("/registration/", methods=["POST","GET"])
def register():
    return render_template('register.html', utitle = "Register")

@app.route("/regauth/", methods=["POST", "GET"])
def regauth():
	form = request.form;
	user = hashlib.sha1(form['user']).hexdigest()
	password = hashlib.sha1(form['password']).hexdigest()
	with open('data/accounts.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if (user == row[0]):
				return render_template('register.html', message = 'Username already registered!' , title = 'Register')
	f.close()

	fd = open('data/accounts.csv','a')
	fd.write(user + ',' + password)
	fd.close()
	return render_template('register.html', message = 'Account Registered!' , title = 'Register')


@app.route("/authenticate", methods=['POST','GET'])
def authenticate():
    inputUser = request.form['username']
    inputPass = request.form['password']
    user = hashlib.sha1(inputUser).hexdigest()
    pw = hashlib.sha1(inputPass).hexdigest()
    with open('data/accounts.csv','rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if (user == row[0] and pw == row[1]):
                f.close()
                return render_template('authenticate.html', utitle = "Death Star destroyed", flag = 1)
    f.close()
    return render_template('authenticate.html', utitle = "RIP Porkins", flag = 0)

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
