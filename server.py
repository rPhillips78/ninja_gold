from flask import Flask, render_template, redirect, session, request
import random
import datetime
app = Flask(__name__)
app.secret_key = "Howmuchistoomany?"


@app.route('/')
def home():
    if 'activities' not in session:
        session['activities'] = []
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', color=session['color'])


@app.route('/process_money', methods=['POST'])
def process():

    if request.form['building'] == "farm":
        winnings = random.randrange(10, 21)
        activity = f"<p style='color:green'>Earned {winnings} from {request.form['building']} at {datetime.datetime.now()}</p>"
        session['activities'].append(activity)

    elif request.form['building'] == "cave":
        winnings = random.randrange(5, 11)
        activity = f"<p style='color:green'>Earned {winnings} from {request.form['building']} at {datetime.datetime.now()}</p>"
        session['activities'].append(activity)
    elif request.form['building'] == "house":
        winnings = random.randrange(2, 6)
        activity = f"<p style='color:green'>Earned {winnings} from {request.form['building']} at {datetime.datetime.now()}</p>"
        session['activities'].append(activity)
    else:
        winnings = random.randrange(-50, 50)
        if winnings < 0:
            activity = f"<p style='color:red'>Earned {winnings} from {request.form['building']} at {datetime.datetime.now()}</p>"
        else:
            activity = f"<p style='color:green'>Earned {winnings} from {request.form['building']} at {datetime.datetime.now()}</p>"
        
        session['activities'].append(activity)

    session['gold'] += winnings

    return redirect('/')


app.run(debug=True)
