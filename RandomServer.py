# encoding: utf-8

import Log as log
import flask
import random
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient
import datetime

logger = log.init_logger("pymodel")
executor = ThreadPoolExecutor(2)

app = flask.Flask(__name__)

@app.route('/get-score', methods=['GET'])
def get_status():
    client = MongoClient('mongo', 27017)
    db = client.counter
    db.col.insert_one({"visit_entry": datetime.datetime.utcnow()})
    logger.info(db.col.count())
    return flask.jsonify({'result': 'OK', 'value': random.random(), 'visit_count': db.col.count()})


@app.route('/health', methods=['GET'])
def service_check():
    return flask.jsonify({'result': 'OK'})
