from flask import Flask, render_template, session, redirect, request
from utils import *
import random

app = Flask(__name__)
app.key = random.randrange(0,15678895)
app.secret_key = str(app.key)


@app.route('/')
def index():
    check_session()
    return render_template('index.html', acts=session['activities'])

@app.route('/process_money', methods=['POST'])
def proc_money():
    gold_update(request.form['building'])
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_gold():
    session['total_gold'] = 0
    session['activities'] = []
    return redirect('/')

app.run(debug=True)