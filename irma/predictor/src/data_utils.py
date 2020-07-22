# Numpy and Maths
import numpy
import math
# Tensorflow
import tensorflow

# Globals
NB_INDICATORS = 15
BATCH_SIZE = 9

def have_one_nan(array: numpy.array, line: int):
    for i in range(NB_INDICATORS):
        if math.isnan(array[line][i]) is True:
            return True
    return False

def init_data(array):
    close_data = []
    for i in range(len(array)):
        if i >= len(array):
            break
        if have_one_nan(array, i) is True:
            array = numpy.delete(array, i, axis=0)
            i -= 1
    #print(array)
    for i in range(len(array)):
        close_data.append(array[i][4])
    close_data = numpy.asarray(close_data)
    array = numpy.delete(array, 4, 1)
    return (array, close_data)
#print(array.shape)
#print(close_data.shape)
#print('array:', array)
#print('close_data:', close_data)

def normalize_data(x_array, y_array, scaler):
    x_array = numpy.reshape(x_array, (-1, NB_INDICATORS - 1))
    x_array = scaler.fit_transform(x_array)

    y_array = numpy.reshape(y_array, (-1, 1))
    y_array = scaler.fit_transform(y_array)
    y_array = numpy.ndarray.flatten(y_array)
    return (x_array, y_array)

def denormalize_data(x_array, y_array, scaler):
    x_array = numpy.reshape(x_array, (-1, 1))
    x_array = scaler.inverse_transform(x_array)
    x_array = numpy.ndarray.flatten(x_array)

    y_array = numpy.reshape(y_array, (-1, 1))
    y_array = scaler.inverse_transform(y_array)
    y_array = numpy.ndarray.flatten(y_array)
    return (x_array, y_array)

def split_data(open_data: numpy.array, close_data: numpy.array):
    x_train = open_data[0 : int(len(open_data) * 0.9)]
    y_train = close_data[0 : int(len(close_data) * 0.9)]
    x_test = open_data[int(len(open_data) * 0.9) : len(open_data)]
    y_test = close_data[int(len(close_data) * 0.9) : len(close_data)]
    return x_train, y_train, x_test, y_test

def batch_data(x_train: numpy.array, y_train: numpy.array):

    dataset = tensorflow.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.batch(BATCH_SIZE)
    (shuffle_open_data, shuffle_close_data) = list(zip(*list(dataset.as_numpy_iterator())))
    return numpy.array(shuffle_open_data), numpy.array(shuffle_close_data)

def unbatch_data(x_train: numpy.array, y_train: numpy.array):

    dataset = tensorflow.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.unbatch()
    (shuffle_open_data, shuffle_close_data) = list(zip(*list(dataset.as_numpy_iterator())))
    return numpy.array(shuffle_open_data), numpy.array(shuffle_close_data)

def shuffle_data(x_train: numpy.array, y_train: numpy.array):

    dataset = tensorflow.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.shuffle(len(y_train), reshuffle_each_iteration=True)
    (shuffle_open_data, shuffle_close_data) = list(zip(*list(dataset.as_numpy_iterator())))
    return numpy.array(shuffle_open_data), numpy.array(shuffle_close_data)