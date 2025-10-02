import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET', 'dev-secret-key')
app.config['SESSION_COOKIE_SECURE'] = False

from application import routes


