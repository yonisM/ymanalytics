from flask import Flask, render_template, request
from forms import SignUpForm
from forms import LoginForm
import os

app = Flask(__name__)



SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#Routes to the index
@app.route("/")
def index():
    return render_template('index.html')

    
#Creates the about page
@app.route("/about")
def about():
    return render_template('about.html', author='Yonis', sunny=False)
    
#creates the blog page 
@app.route("/blog")
def blog():
    posts = [
    {'title': "The book of worms", 'author': 'Yonis Mohamoud'}, 
    {'title': "Harry Potter", 'author': 'J.K Rowley'},
    {'title': "Secret tales", 'author': 'Perhaps Injay'}
    ]
    return render_template('blog.html', posts=posts)
       
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