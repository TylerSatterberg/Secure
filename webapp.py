import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/tryagain')
def tryagain():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/p1')
def renderP1():
    return render_template('p1.html')

@app.route('/p2',methods=['GET','POST'])
def renderP2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/p3',methods=['GET','POST'])
def renderP3():
    session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)
