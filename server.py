from flask import Flask, render_template, request
from forms import SignUpForm
from forms import LoginForm
from search import search_string
import pandas as pd
import numpy as np
import os

app = Flask(__name__)



#Randomly generate secret keys
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#Routes to the index
@app.route("/")
def index():
    return render_template('index.html')


#creates the search page 
@app.route("/search", methods=['GET','POST'])
def search():
    
    if request.method == 'POST':
        display = 'block'
        values = request.form['search']
        shortened_list, count = search_string(values)
        return render_template('search_data.html', shortened_list=shortened_list, count=count, display=display)
    else:
        display = "none"
        return render_template('search_data.html', display=display)




    
#Creates a blog entry page
@app.route("/blog/<blog_id>")
def blogpost(blog_id):
    return "This is the blog entry " + str(blog_id)
    
    
#Creates the sign up page
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        return render_template('user.html', result=result, fullname=fullname, email=email)
    
    return render_template('signup.html', form=form)

#Creates the log in page 
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')
    

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    


    

if __name__== '__main__':
    app.run()