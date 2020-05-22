# Matplotlib
import matplotlib.pyplot
# Tensorflow
import tensorflow
# Numpy and Pandas
import numpy
import pandas
# Ohter import
import sys
import os

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

EPOCHS = 10
DATA_SAMPLE = 1000

def init_data(stocks_path):
    dirs = os.listdir(stocks_path)
    file = dirs[2]
    data = pandas.read_csv(os.path.join(stocks_path, file)).to_numpy()
    open_data = []
    close_data = []
    for i in range(DATA_SAMPLE):
        open_data.append(data[i][1])
    for i in range(DATA_SAMPLE):
        close_data.append(data[i][1])
    open_data = numpy.asarray(open_data)
    close_data = numpy.asarray(close_data)
    return (open_data, close_data)

def normalize_data(x_array, y_array):
    x_array = numpy.divide(
                    numpy.subtract(x_array, numpy.mean(x_array)),
                    numpy.nanstd(x_array)
                )
    y_array = numpy.divide(
                    numpy.subtract(y_array, numpy.mean(y_array)),
                    numpy.nanstd(y_array)
                )
    return (x_array, y_array)

def denormalize_data(x_array, y_array):
    x_array = numpy.divide(
                    numpy.nanstd(x_array),
                    numpy.subtract(x_array, numpy.mean(x_array))
                )
    y_array = numpy.divide(
                    numpy.nanstd(y_array),
                    numpy.subtract(y_array, numpy.mean(y_array))
                )
    return x_array, y_array

def create_model():
    model = tensorflow.keras.models.Sequential()
    model.add(tensorflow.keras.layers.Dense(5, input_shape=(1,)))
    model.add(tensorflow.keras.layers.Dense(1, input_shape=(1,)))

    ##input_layer = tensorflow.keras.layers.Input((1, ))
    ##dense1_layer = tensorflow.keras.layers.Dense(units=1, input_shape=(1,))
    ##output = dense1_layer(input_layer)
    ##model = tensorflow.keras.Model(inputs=input_layer, outputs=output)
    #model.summary()
    model.compile(
        loss="mean_squared_error",
        optimizer=tensorflow.keras.optimizers.Adam(0.1),
    )
    return (model)

def print_predict(predict, real):
    """printing predict"""
    matplotlib.pyplot.plot(predict, 'r')
    matplotlib.pyplot.plot(real, 'b:')
    matplotlib.pyplot.title("Predict")
    matplotlib.pyplot.show()

def predict_on_stocks(stocks_path: str, store_path: str, models_path: str):
    open_data, close_data = init_data(stocks_path)
    open_data, close_data = normalize_data(open_data, close_data)
    x_train, x_test, y_train, y_test = train_test_split(open_data, close_data, test_size=0.10, random_state=42)

    model = create_model()
    model.fit(x_train, y_train, epochs=EPOCHS)
    predicted_data = model.predict(x_test)
    real_data = y_test
    #predicted_data, real_data = denormalize_data(predicted_data, real_data)
    print_predict(predicted_data, real_data)
