list=[1,3,4,5,6,7,8,9,10,11,12,13,2]
from flask import Flask, render_template, url_for, flash, redirect
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '90d29299e6c6ffddeba3ac23230e125c'

# dummy data
posts = [
    {'author': 'Frank Edwardgggggg',
     'title': 'First blog post',
     'content': 'This is my very first post',
     'date': 'Oct 4,2029'
     },
    {'author': 'Mike Ben',
     'title': 'Second Blog Post',
     'content': 'This is my very second post',
     'date': 'Oct 9,2029'
     },
    {'author': 'alice Ben',
   
    {'author': 'Mike Ben',
     'title': 'Second Blog Post',
     'content': 'This is my very second post',
     'date': 'Oct 9,2029'
     },
   {'author': 'Mike Ben',
     'title': 'Second Blog Post',
     'content': 'This is my very second post',
     'date': 'Oct 9,2029'
     },
{'author': 'Mike Ben',
     'title': 'Second Blog Post',
     'content': 'This is my very second post',
     'date': 'Oct 9,2029'
     },
{'author': 'Mike Ben',
     'titleyyhsjssj': 'Second Blog Post',
     'content': 'Thihhhs is my very second post',
     'date': 'Oct 9,2029'
     },

{'author': 'Mike Ben',
     'title': 'Second Blog Post',
     'content': 'This is my very second post',
     'date': 'Oct 9,2029'
     },
    
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', items=posts, title=home)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/just", methods=['POST', 'GET'])
def just():
    #form = RegistrationForm()
    #if form.validate_on_submit():
        #flash(f"You have been register successfully {form.username.data}!", 'success')
        #return redirect(url_for('home'))
    return render_template('just.html', title='register',)


@app.route("/register", methods=['POST', 'GET'])
def register():
    #form = RegistrationForm()
    #if form.validate_on_submit():
        #flash(f"You have been register successfully {form.username.data}!, please procceed to login😊", 'success')
        #return redirect(url_for('login'))
    return render_template('register.html', title='register',)


@app.route("/login", methods=['POST', 'GET'])
def login():
    #form = LoginForm()

    #if form.email.data == "admin@gmail.com" and form.password.data == "1234":
       # flash(f"Welcome {form.email.data}!, Check what's New on the Site😊", 'success')
        #return redirect(url_for('home'))
    return render_template('login.html', title='login')


if __name__ == '__main__':
    app.run(debug=True)

