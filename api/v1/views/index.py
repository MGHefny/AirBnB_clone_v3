#!/usr/bin/python3
"""ind"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def api_stat():
    """ check """
    return jsonify({'status': 'OK'})
