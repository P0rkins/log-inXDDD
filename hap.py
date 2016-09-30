from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    print app
    print request
    print request.args
    #print request.args['username'] #if username submitted
    #print request.headers          #only works for POST
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST'])
def authenticate():
    username = "P0rkins"
    password = "red6"
    inputUser = request.form['username']
    inputPass = request.form['password']
    if username == inputUser and password == inputPass:
        utitle = "You can hold it!"
        utext = "Death Star Destroyed."
    else:
        utitle = "Ahhhh"
        utext = "RIP Porkins"

    return render_template("success.html", title = utitle, text = utext)

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
