from flask import Flask, render_template, request, session, url_for
import hashlib
app = Flask(__name__)
app.secret_key = "XDDD"

d={}
user=""

@app.route("/")
def login():
    convertDict()
    if(user in session):
        return welcome()
    else:
        return login()

@app.route("/login/", methods=["POST"])
def login():
    return render_template('login.html', utitle = "Register")

@app.route("/regauth/", methods=["POST", "GET"])
def regauth():
	form = request.form;
	user = hashlib.sha1(form['user']).hexdigest()
	password = hashlib.sha1(form['password']).hexdigest()
	with open('data/accounts.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if (user == row[0]):
				return render_template('register.html', message = 'Already registered!' , title = 'Register')
	f.close()

	fd = open('data/accounts.csv','a')
	fd.write(user + ',' + password)
	fd.close()
	return render_template('register.html', message = 'Account Registered!' , title = 'Register')


@app.route("/auth", methods=['POST'])
def authenticate():
    global user
    convertDict()
    if request.method=="POST":
        u=request.form["username"]
        user=u
        p=hashIt(request.form["pass"])
        if u in d.keys():
            if p==d[u][:56]:
                session[user]=p
                return welcome()
            else:
                return render_template("login.html",message="Hmm... it seems that your password was incorrect. try again.")
        else:
            return render_template("login.html",message="Hmm... that username doesn't seem to exist.")
        return "All green"

@app.route("/register/",methods=["POST"])
def registration():
    if request.method=="POST":
        u=request.form["username"]
        p=hashbrowns(request.form["pass"])
        if u in d.keys():
            return render_template("login.html",message="Username taken. Be more original")
        else:
            if len(u) < 1 or len(p) < 1:
                return render_template("login.html",message="You suck at being creative. Have a better username or password")
            else:
                addAccount(u,p)
                convertDict()
                return render_template("login.html",message="Success! Your account has been created.")
        return "YES"

@app.route("/welcome/",methods=["POST"])
def welcome():
    return render_template("loggedin.html", message="Logged in, "+user+"!")

@app.route("/secretgate/")
def other():
    if(user in session):
        return render_template("secretgate.html", message="You are logged in as "+user+".")
    else:
        return render_template("secretgate.html", message="You are not logged in")

@app.route("/logout/",methods=["POST"])
def logout():
    if(user in session):
        session.pop(user)
    return home()

#helpers
def convertDict():
    f = open("data/accounts.csv")
    f.readline()
    m = f.readline()
    while m!='':
        n = m.index(',')+1
        d[m[:n-1]] = m[n:]
        m = f.readline()
    return d

def hashIt(x):
    return hashlib.sha224(x).hexdigest()

def addAccount(u,p):
    fd = open('data/accounts.csv','a')
    fd.write(u+","+p+"\n")
    fd.close()
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
