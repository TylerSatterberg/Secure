import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import time
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
def renderp1():
    session["start_time"] = time.time()
    return render_template('p1.html')

@app.route('/p2',methods=['GET','POST'])
def renderp2():
    session["Equilibrium"]=request.form['Equilibrium']
    return render_template('p2.html')

@app.route('/p3',methods=['GET','POST'])
def renderp3():
    session["avacado"]=request.form['avacado']
    return render_template('p3.html')

@app.route('/p4',methods=['GET','POST'])
def renderp4():
    session["sigfig"]=request.form['sigfig']
    return render_template('p4.html')
    
@app.route("/p5", methods=['GET', 'POST'])
def renderp5():
    session["end_time"] = time.time()
    T = session["end_time"] - session["start_time"]
    session["Ksp"]=request.form['Ksp']
    t=0
    if session["Equilibrium"] == "A physical change occurs, and solvation is exothermic":
        t = t + 1 
    else:
        t = t
        
    if session["avacado"] == "6.022x10^23":
        t = t + 1 
    elif session["avacado"] == "6.02x10^23":
        t = t + 0.5
    else:
        t = t
        
    if session["sigfig"] == "6 figures":
        t = t + 1 
    else:
        t = t
        
    if session["Ksp"] == "3.0x10^-4":
        t = t + 1 
        print("t")
    else:
        t = t
    Time = round(T, 0)
    return render_template('p5.html', total=t, Time=Time)

if __name__=="__main__":
    app.run(debug=True)
