#!/usr/bin/python3
"""ind"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def api_stat():
    """ check """
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def count_stats():
    '''check'''
    stats_count = {}
    for cls in classes:
        stats_count[cls] = storage.count(classes[cls])
    return jsonify(stats_count)



#!/usr/bin/python3
"""host and port"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


ap = Flask(__name__)

ap.register_blueprint(app_views)


@app.teardown_appcontext
def cls_engn(self):
    """clos engen"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """error 404"""
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    x = getenv('HBNB_API_HOST', '0.0.0.0')
    y = int(getenv('HBNB_API_PORT', 5000))
    ap.run(host=x, port=y, threaded=True)
