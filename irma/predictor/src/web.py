#!/usr/bin/env python3

from flask import Flask, jsonify, request
import tensorflow
import numpy
import math
import simplejson as json

from main import *
from predict import *
from data_utils import *

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 8080
DEBUG = True

MODELS_PATH = "../models"
NB_INDICATORS = 15

def prepare_prediction(array: numpy.array):
    scaler = StandardScaler()
    array = normalize_data(array, array, scaler, NB_INDICATORS + 1)[0]
    open_data = array[len(array) - 1]
    open_data[1] = open_data[4]
    open_data = numpy.delete(open_data, 4, 0)
    return (open_data)

def transform_nan(stocks_data: numpy.array):
    stocks_data = stocks_data.tolist()
    for y in range(len(stocks_data)):
        for i in range(len(stocks_data[y])):
            if math.isnan(stocks_data[y][i]):
                stocks_data[y][i] = None
    return (stocks_data)

@app.route("/", methods=["GET", "POST"])
def hello():
    stock_symbol = None
    model = None
    interval = None

    if request.args.get("stock") is not None:
        stock_symbol = str(request.args["stock"])
        interval = str(request.args["interval"])
        model_path = f'{MODELS_PATH}/model_{stock_symbol}_{interval}'

        (stocks_data, scaler) = generate_model_on_stock(stock_symbol, interval)
        to_predict_data = numpy.array(prepare_prediction(stocks_data))
        stocks_data = numpy.array(stocks_data)

        model = tensorflow.keras.models.load_model(model_path)
        predict = predict_one_interval(model, to_predict_data, scaler).tolist()

        stocks_data = scaler.inverse_transform(stocks_data)

        stocks_data = numpy.delete(stocks_data, numpy.s_[7:NB_INDICATORS - 1], axis=1)
        stocks_data = numpy.array(transform_nan(stocks_data))
        stocks_data = stocks_data.tolist() + predict
        return jsonify(stocks_data)
    else:
        return jsonify('Please enter a stock symbol and an interval in the URL')

if __name__ == "__main__":
    app.run(host=HOST, debug=DEBUG)