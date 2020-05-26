from flask import request
from src import app
from src.models import Model
import simplejson
import ndjson
import pandas as pd

# initialize the model
AQS = Model()


def json_dumps(data):
    return simplejson.dumps(data, ensure_ascii=False, ignore_nan=True)


@app.route('/get')
def get():
    return json_dumps('get')

@app.route('/getdata')
def getdata():
    return json_dumps(AQS.getData())


@app.route('/get_data_by_param')
def getdatabyparam():
    return json_dumps(AQS.getDataByParam('pm25'))


@app.route('/post', methods=['POST'])
def post():
    post_data = request.data.decode()
    if post_data != "":
        post_data = simplejson.loads(post_data)
    return json_dumps(post_data)