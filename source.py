from flask import Flask,render_template,make_response,request,redirect,url_for,Response,session,flash,Response,send_file
from flask_mail import Mail,Message
from pymongo import MongoClient
import json
import urllib
import datetime
import threading,jinja2
import os
import binascii
from bson import ObjectId
from ldap3 import Server,Connection,ALL
from functools import wraps
import datetime,random
mongo = MongoClient('mongodb+srv://cmsnoc93:'+ urllib.parse.quote('cmsnoc@123') + '@cluster0-qxw77.mongodb.net/test?retryWrites=true&w=majority')
db = mongo.Engineer_Dashboard
onb_cand = db.Onboarded_Candidates
cand =  db.Candidates
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/login',methods = ['GET','POST'])
def login1():
    # if session and session['logged_in']:
    #     return redirect(url_for('landing'))
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
                if request.form['cec'] == 'araviana' and request.form['password'] == 'araviana':
                    session['logged_in'] = True
                    session['role'] = 'manager'
                    session['username'] = request.form['cec']
                    return redirect(url_for('landing'))
                elif request.form['cec'] == 'neemenon' and request.form['password'] == 'neemenon':
                    session['logged_in'] = True
                    session['role'] = 'technical'
                    session['username'] = request.form['cec']
                    return redirect(url_for('landing'))
                elif request.form['cec'] == 'ritpande' and request.form['password'] == 'ritpande':
                    session['logged_in'] = True
                    session['role'] = 'engineer'
                    session['username'] = request.form['cec']
                    return redirect(url_for('landing'))
                else:
                    flash("Invalid Password", 'log_msg')
                    return redirect(url_for('login1'))
                return redirect(url_for('landing'))

@app.route('/landing',methods=['GET','POST'])
def landing():
    return render_template('landing.html')

@app.route('/save',methods = ['POST'])
def save():
    if request.method == 'POST':
        webex = request.form.get('webex', None)
        finesse = request.form.get('finesse', None)
        cmsp = request.form.get('cmsp', None)
        splunk = request.form.get('splunk', None)
        vdi = request.form.get('vdi', None)
        ncm = request.form.get('ncm', None)
        sevone = request.form.get('sevone', None)
        eigrp = request.form.get('eigrp', None)
        ospf = request.form.get('ospf', None)
        cand.insert({'name':session['username'],'webex':webex,'finesse':finesse,'cmsp':cmsp,'splunk':splunk,'vdi':vdi,'ncm':ncm,'sevone':sevone,'eigrp':eigrp,'ospf':ospf})
    return 'Thanks for your feedback!'

@app.route('/start',methods = ['POST'])
def start():
    candis = cand.find()
    return render_template('start.html', candis=candis)