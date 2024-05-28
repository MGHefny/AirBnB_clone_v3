#!/usr/bin/python3
"""host and port"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


ap = Flask(__name__)

ap.register_blueprint(app_views)


@app.teardown_appcontext
def cls_engn(exception):
    """clos engen"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """error 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    x = getenv("HBNB_API_HOST", "0.0.0.0")
    y = int(getenv("HBNB_API_PORT", 5000))
    ap.run(debug=True, host=x, port=y, threaded=True)
