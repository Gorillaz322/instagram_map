from flask import Flask
from flask_oauth import OAuth

import settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

oauth = OAuth()
instagram = oauth.remote_app(
    'instagram',
    base_url='https://api.instagram.com/',
    request_token_url=None,
    access_token_url='https://api.instagram.com/oauth/access_token',
    authorize_url='https://api.instagram.com/oauth/authorize',
    consumer_key=settings.INST_CLIENT_ID,
    consumer_secret=settings.INST_CLIENT_SECRET,
    request_token_params={'response_type': 'code'},
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'}
)

import main.views
import main.models
