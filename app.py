# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
import model
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
	date = model.getDateString(datetime.now())
	return render_template('index.html', time = datetime.now(), date=date)


@app.route('/results', methods=['GET','POST'])
def results():
	if request.method=='POST':
		# print(request.form['color'])
		name = request.form['name']
		user_color = request.form['color']
		user_pizza = request.form['pizza']
		user_animal = request.form['animal']
		user_subject = request.form['subject']
		user_book = request.form['book']
		winner = model.tallyPoints(user_color, user_pizza, user_animal, user_subject, user_book)
		pic = model.getImage(winner)
		site = model.getUrl(winner)
		date = model.getDateString(datetime.now())
		return render_template('/results.html', name=name, winner = winner, pic=pic, site=site, date=date)
	else:
		return redirect('/')
