import os
import pandas
pandas.set_option('mode.chained_assignment', None)
import numpy
from stockstats import StockDataFrame
from sklearn.preprocessing import StandardScaler

INDICATORS = ['change', 'volume_delta', 'open_2_sma', 'adx_6_ema', 'macdh', 'boll_ub', 'boll_lb', 'rsi_12', 'pdi']

def add_indicator(array, values):
    bools = []
    for i in range(array.shape[0]):
        bools.append(values[i])
    array = numpy.array(array)
    array.resize((array.shape[0], array.shape[1] + 1))
    for i in range(array.shape[0]):
        array[i][array.shape[1] - 1] = bools[i]
    return array

def manage_stocks(stock_path: str):
    stock = pandas.read_csv(stock_path)
    stock_stats = StockDataFrame.retype(stock)
    array = numpy.array(stock)
    for i in range(len(INDICATORS)):
        array = add_indicator(array, stock_stats[INDICATORS[i]].to_numpy())
    return array

def add_indicators_to_predict(stock_path: str):
    stock = pandas.read_csv(stock_path)
    stock_stats = StockDataFrame.retype(stock)
    array = numpy.array(stock)
    for i in range(len(INDICATORS)):
        array = add_indicator(array, stock_stats[INDICATORS[i]].to_numpy())

    array = StandardScaler().fit_transform(array)
    close_data = numpy.reshape(array[len(array) - 1], (-1, len(array[len(array) - 1])))
    return close_data