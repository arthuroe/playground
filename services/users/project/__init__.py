# services/users/project/__init__.py
import os

from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

from .models import db

db.init_app(app)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
