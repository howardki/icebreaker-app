from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Howard'}
    posts = [
        {
            'author': {'username': 'Dominic'},
            'body': 'How does flask work'
        },
        {
            'author': {'username': 'Katherine'},
            'body': 'You two are useless :/'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
    # ...