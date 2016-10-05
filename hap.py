from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route("/")
def login():
    print request.headers          #only works for POST
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST','GET'])
def authenticate():
    username = "P0rkins"
    password = "red6"
    inputUser = request.form['username']
    inputPass = request.form['password']
    if username == inputUser and password == inputPass:
        return render_template('authenticate.html', utitle = "Death Star destroyed", flag = 1)
    else:
        return render_template('authenticate.html', utitle = "RIP Porkins", flag = 0)

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
