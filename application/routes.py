from werkzeug.security import check_password_hash
from flask import render_template, request, redirect, url_for
import random
import os
import jwt
import datetime
from functools import wraps
from flask import render_template, request, redirect, url_for, make_response, jsonify
from application import app
from application.data_access import get_joke, get_jokes_count, get_user, add_user
import bcrypt

@app.route('/logout/submit', methods=['POST'])
def submit_logout():
    print("REACHED")
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('token', '', expires=0)
    return resp

@app.route('/logout')
def logout():
   return render_template('logout.html', title="logout" ) 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('login'))
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[JWT_ALGORITHM])

            return f(*args, **kwargs, user=payload['user'])
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
    return decorated_function


@app.route('/dashboard')
@login_required
def dashboard(user=None):
    return render_template('welcome.html', title='Dashboard', name=user, group='Authenticated Users')


from application.data_access import get_joke, get_jokes_count, add_joke_to_database

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<string:name>')
def welcome(name='Team'):
    return render_template('welcome.html', title="Welcome", name=name.title(), group='Everyone')


@app.route('/joke')
def joke():
    joke = get_joke()
    count = get_jokes_count()
    return render_template('joke.html', title="Joke Time", joke_question=joke[1], joke_answer=joke[2], number_of_jokes=count[0])

joke_dict = {0: ["Why was Cinderella so bad a football?", "She kept running away from the ball!"],
             1: ["What do you call a pile of cats?", "A meow-ntain"],
             2: ["Why did the bicycle fall over?", "Because it was two tired"],
             3: ["What do you call a sad strawberry?", "A blueberry!"],
             4: ["How do you organise a space party?", "You planet."],
             5: ["What do cows read the most?", "Cattle-logs."],
             6: ["What do clouds wear under their shorts?", "Thunder pants!"],
             7: ["What did 0 say to 8?", "Nice belt."],
             8: ["What did the drummer name her twin daughters?", "Anna 1, Anna 2."],
             9: ["How does the moon cut his hair?", "Eclipse it."],
             10: ["Why did the scarecrow win an award?", "Because he was outstanding in his field."],
             11: ["What’s brown and sticky?", "A stick."],
             12: ["What do you call a sad cup of coffee?", "Depresso."],
             13: ["Why didn't the melons get married?", "Because they cantaloupe."],
             14: ["What goes up and down but doesn’t move?", "Stairs."],
             15: ["What do you get when you cross a fish and an elephant?", "Swimming trunks."],
             16: ["Why can’t a nose be 12 inches long?", "Because then it would be a foot."],
             17: ["What do you call a magician that loses his magic?", "Ian."],
             18: ["How do rabbits travel?", "By hareplanes."],
             19: ["What do you call a sleeping dinosaur?", "A dino-snore."],
             20: ["Why did the strawberry cry?", "He found himself in a jam."]
             }

       
@app.route('/hello')
def hello():
    return render_template('hello.html', title='Hello')



# Secret key for JWT encoding/decoding (will use env later)
JWT_SECRET = os.getenv('JWT_SECRET', 'dev_secret_key')
JWT_ALGORITHM = 'HS256'

@app.route('/login')
def login():
    token = request.cookies.get('token')
    if token:
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return redirect(url_for('logout'))
        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass
    return render_template('login.html', title='Login')

@app.route('/login/submit', methods=['POST'])
def submit_login():
    print("login POST received")
    
        
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_bytes = password.encode('utf-8')
        user = get_user(username)
        hashed_pass_bytes = user[2].encode('utf-8')
        print(f"User lookup for '{username}': {user}")
        if user and username == user[1] and bcrypt.checkpw(password_bytes, hashed_pass_bytes):
            token = jwt.encode({
                'user': username,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            response = make_response(redirect(url_for('logout')))
            response.set_cookie('token', token, httponly=True, secure=False)
            print("logged in")
            return response

    return redirect(url_for('login'))

@app.route('/add-joke')
@login_required
def add_joke(user):
    return render_template('add_joke.html', title='Add Joke')

@app.route('/add-joke/submit', methods=['POST'])
def submit_joke():
    setup = request.form['setup']
    punchline = request.form['punchline']


    add_joke_to_database(setup, punchline)
    print(f"added joke: {setup}, {punchline}")
    return redirect(url_for('add_joke'))

    
@app.route('/register')
def register():
    return render_template('add_user.html', title="Register")

@app.route('/register/submit', methods=['POST'])
def submit_register():
    if request.method == 'POST':
        username = request.form.get('username')    
        password = request.form.get('password')
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()

        hashed_pass = bcrypt.hashpw(password_bytes, salt)

        add_user(username, hashed_pass)
    
    return redirect(url_for('register'))



@app.route('/error/<int:code>')
def error_code(code):
    error_messages = {
        404: 'Resource not found.',
        500: 'Internal server error.',
        403: 'Forbidden.',
        401: 'Unauthorized.',
    }
    message = error_messages.get(code, 'Unknown error.')
    return jsonify({
        'status': 'error',
        'code': code,
        'message': message
    }), code

@app.route('/user/<string:username>')
def user_info(username):
    user = get_user(username)
    if user:
        return jsonify({
            'status': 'success',
            'data': {
                'id': user[0],
                'username': user[1],
                'roles': ['user']
            }
        })
    return jsonify({
        'status': 'error',
        'message': 'User not found.'
    }), 404