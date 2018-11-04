from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import Classroom
from flask_login import current_user, login_user
import pdb

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
            'body': 'You two are USEFUL1 :/'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
        # return redirect(url_for('index'))
    print("login")
    form = LoginForm()
    # pdb.set_trace()
    if form.validate_on_submit():
        print("i've hit form.validate_on_subtmi")
        c = Classroom.query.filter_by(id=int(form.password.data)).first()
        if c is None:
            flash('Invalid class ID.')
            return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    # console.log("loading login")
    return render_template('login.html', title='Sign In', form=form)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return
