from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='damascusVIII'

@app.route('/')
def number_game():
    if 'random' not in session:
        session['random']=random.randint(1,100)

    if 'guesses' not in session:
        session['guesses']=0

    if 'check' not in session:
        session['check']='start'  
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/submit", methods=['POST'])
def submitGuess():
    session['guess']=int(request.form['guess'])
    if session['guess'] > session['random']:
        session['check'] = 'high'
        session['guesses']+= 1
    elif session['guess'] < session['random']:
        session['check'] = 'low'
        session['guesses']+= 1
    else:
        session['check'] = 'correct'
        session['guesses']+= 1
    
    if session['guesses']==5 and session['check']!='correct':
        session['check']='gameover'
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)