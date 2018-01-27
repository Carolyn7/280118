from flask import Flask, render_template, request, session, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, PasswordField ,validators
import MainPromo
import datetime
import mainRewards

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('featured.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/learn1')
def learn1():
    return render_template('learn.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/calculator1')
def calculator1():
    return render_template('calculator.html')

@app.route('/calculator2')
def calculator2():
    return render_template('calculator.html')

@app.route('/details')
def details():
    session["Username"] = "John"
    userslist = []
    userslist = MainPromo.ProcessUser()
    card_type = MainPromo.ActualUser(session["Username"])
    return render_template('details.html', userslist = userslist, card_type = card_type,name=session["Username"])

@app.route('/rewards')
def reward():
    session['userid'] = 'John'
    total = mainRewards.ProcessTransaction(session['userid'])
    dateList = mainRewards.ProcessDate(session['userid'])
    pt = mainRewards.get_point(session["userid"])
    flash('You are left with ' + pt + " points in total")
    return render_template('rewards.html', totalDeduct = total, dateList = dateList)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()





