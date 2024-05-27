#!/usr/bin/python3
"""host and port"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == '__main__':
    x = getenv('HBNB_API_HOST', '0.0.0.0')
    y = int(getenv('HBNB_API_PORT', 5000))
    HBNB_API_PORT = 5000
    app.run(host=x, port=y, threaded=True)
