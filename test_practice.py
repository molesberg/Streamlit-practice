import numpy as np
import pytest
mySeed = 42

def func(mySeed):
    np.random.seed(mySeed)
    array = np.random.rand(10, 10)
    maxColumn = np.argmax(np.sum(array, axis = 0))
    minColumn = np.argmin(np.sum(array, axis = 0))
    return array, maxColumn, minColumn

def test_columns_pass():
    array, maxColumn, minColumn = func(mySeed)
    assert np.sum(array[:, maxColumn]) > np.sum(array[:, minColumn])


def test_columns_fail():
    array, maxColumn, minColumn = func(mySeed)
    assert np.sum(array[:, maxColumn]) <= np.sum(array[:, minColumn])
