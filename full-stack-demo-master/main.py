
from flask import Flask, render_template #imports flask and flask CORS (this allows us to make our
from flask_cors import CORS #server)
app = Flask(__name__) #initializes the app

from config import Config
from forms import LoginForm

app.config['SECRET_KEY'] = 'everything is magic'
app.config.from_object(Config)

CORS(app) #allows cross-origin sharing (meaning anyone can send requests to the app)
counter = 0 #this makes counter global (we need this so that when a user changes counter it persists and doesn't get set back to 0 every time).

@app.route('/')
@app.route('/index')
def index():  # pragma: no cover #this loads index.html as the primary web page
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/counter', methods=['GET']) #this creates a route called /counter that we can reference in the front end called /counter and makes it a get method
def get_counter(): #this function returns counter as a string
        global counter
        return str(counter), 200

@app.route('/add', methods=['POST'])#this creates a route that we can reference in the front end called /add and makes it a post method
def add_1(): #adds one to counter (remember this doesn't display counter, the         front-end needs to deal with this
        global counter
        counter = counter + 1
        return '', 200

@app.route('/subtract', methods=['POST'])
def subtract_1(): #subtracts one from counter (also doesn't display counter)
        global counter
        counter = counter - 1
        return '', 200

@app.route('/login/signinUser', methods=['POST'])
def add_user():
        if form.validate_on_submit():
                print("i've hit form.validate_on_submit")
                c = Classroom.query.filter_by(id=int(form.password.data)).first()
                if c is None:
                        flash('Invalid class ID.')
                        return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
                return redirect(url_for('index'))
        else:
                return render_template('login.html', title='Sign In', form=form)
    # console.log("loading login")


    
