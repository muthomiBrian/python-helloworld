import logging

from flask import Flask, jsonify
from datetime import datetime

logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello():
    log_request('hello')
    return "Hello World!"


@app.route("/status")
def status():
    log_request('status')
    return jsonify({
        'result': 'OK - Healthy',
    })


@app.route("/metrics")
def metrics():
    log_request('metrics')
    return jsonify({
        'data': {
            'UserCount': 140,
            'UserCountActive': 23,
        }
    })


def log_request(endpoint_name):
    timestamp = datetime.utcnow()
    logging.debug(f"{timestamp}, {endpoint_name} endpoint was reached")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
