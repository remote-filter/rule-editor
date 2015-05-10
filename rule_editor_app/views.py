import time
from flask import Flask, url_for, session, request, redirect, Response
from rule_editor_app import app, redis, config, gmail
import json

app.secret_key = 'secret'

@app.route('/')
def index():
    user_json = redis.get(session['user_email'])
    if (user_json):
        user = json.loads(user_json)
        print(user)
        return "user email: %s; user token: %s" % (user['user']['email'], user['gmail_token'])
    return 'Hello World!'

@app.route('/login')
def login():
    return gmail.authorize(callback=url_for('authorized', _external=True))

@gmail.tokengetter
def get_gmail_token(token=None):
    print "session.get('gmail_token') %s" % session.get('gmail_token')
    return session.get('gmail_token')

@app.route('/login/authorized')
@gmail.authorized_handler
def authorized(resp):
    print "response \n"
    print(resp)
    print "gmail \n"
    print(gmail)
    print "continue \n"
    session['gmail_token'] = (resp['access_token'],)
    user = gmail.get('userinfo')
    #user = (resp['userinfo'],)
    print("user: %s" % user)
    print("user.data['email']: %s" % user.data['email'])
    session['user_email'] = user.data['email']
    redis.set(session['user_email'], json.dumps({ "user": user.data, "gmail_token": session['gmail_token']}))
    return redirect(url_for('index', _external=True))

