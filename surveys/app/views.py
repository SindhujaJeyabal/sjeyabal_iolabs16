from app import myapp,model
from flask import request, render_template, session, redirect, url_for, escape
import os
import model

myapp.secret_key = os.urandom(24)

@myapp.route('/')
@myapp.route('/index')
def index():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		return render_template('survey.html', name=username)
	else:
		return render_template('login.html')

@myapp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		######## DELETE THIS PART FOR NUM. 3 ###########
		session['username'] = request.form['username']
		session['email'] = request.form['email']
		return redirect(url_for('index'))
		######## DELETE THIS PART FOR NUM. 3 ###########

@myapp.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@myapp.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
	username = ''
	email = ''
	if 'username' in session:
		username = escape(session['username'])
		email = escape(session['email'])
		surveyResponse = {}
		surveyResponse['color'] = request.form.get('color')
		surveyResponse['food'] = request.form.get('food')
		surveyResponse['vacation'] = request.form.get('vacation')
		surveyResponse['fe-before'] = request.form.get('feBefore')
		surveyResponse['fe-after'] = request.form.get('feAfter')
		surveyResponse['interest'] = request.form.get('interest')
		surveyResponse['comment'] = request.form.get('comment')
		#insert code here to send surveyresponse into your mongoDB
		model.insert_result(username, email, surveyResponse)
		return render_template('results.html', name=username, email=email, surveyResponse=surveyResponse)
	else:
		return render_template('login.html')

@myapp.route('/aggregate', methods=['GET', 'POST'])
def aggregate_survey():
	print "In views aggregate"
	survey_deets = model.get_aggregate()
	return render_template('aggregate.html', counter = survey_deets["count"], avg_before = survey_deets['avg_before'], avg_after = survey_deets['avg_after'])

@myapp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
