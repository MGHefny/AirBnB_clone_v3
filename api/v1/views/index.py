#!/usr/bin/python3
"""ind"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def api_stat():
    """ check """
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def api_stats():
    """check"""
    stats = (
        'amenities':storage.count('Amenity'),
        'cities':storage.count('City'),
        'places':storage.count('Place'),
        'reviews':storage.count('Review'),
        'states':storage.count('State'),
        'users':storage.count('User'),
    )
    return jsonify(stats)
