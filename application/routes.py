from flask import render_template, request, redirect, url_for
import random
from application import app
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

@app.route('/add-joke')
def add_joke():
    return render_template('add_joke.html', title='Add Joke')

@app.route('/add-joke/submit', methods=['POST'])
def submit_joke():
    setup = request.form['setup']
    punchline = request.form['punchline']
    
    
    add_joke_to_database(setup, punchline)
    print(f"added joke: {setup}, {punchline}")
    return redirect(url_for('add_joke'))
