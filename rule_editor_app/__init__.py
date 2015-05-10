from flask import Flask
from redis import Redis
import os
import site_config as config
from flask_oauthlib.client import OAuth

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
oauth = OAuth(app)
gmail = oauth.remote_app('gmail',
                         consumer_key=config.GOOGLE_ID,
                         consumer_secret=config.GOOGLE_SECRET,
                         request_token_params={'scope': ['https://www.googleapis.com/auth/gmail.modify',
                                                         'https://www.googleapis.com/auth/userinfo.email'],
                                               'access_type': 'offline'},
                         base_url='https://www.googleapis.com/oauth2/v1/',
                         authorize_url='https://accounts.google.com/o/oauth2/auth',
                         access_token_method='POST',
                         access_token_url='https://accounts.google.com/o/oauth2/token',
                         request_token_url=None)

# gmail = oauth.remote_app(
#                         'gmail',
#                         consumer_key=config.GOOGLE_ID,
#                         consumer_secret=config.GOOGLE_SECRET,
#                         request_token_params={
#                             'scope': ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/userinfo.email']},
#                         base_url='https://www.googleapis.com/oauth2/v1/',
#                         authorize_url='https://accounts.google.com/o/oauth2/auth',
#                         access_token_method='POST',
#                         access_token_url='https://accounts.google.com/o/oauth2/token',
#                         request_token_url=None)

import rule_editor_app.views
