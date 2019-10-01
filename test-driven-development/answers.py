import numpy as np
import pandas as pd


def one_hot(data):
    columns = sorted(set(data))

    values = np.zeros((len(data), len(columns)))

    for row, d in enumerate(data):
        col = columns.index(d)
        values[row, col] = 1
        
    return pd.DataFrame(values, columns=columns)


def test_normalize():
    arr = np.array([[-5, 0], [0, 10], [5, -10]]).astype(np.float32)
    norm = normalize(arr)

    np.testing.assert_array_equal(norm, [[0, 0.5], [0.5, 1], [1, 0]])
    assert norm.shape == arr.shape
    assert (np.min(norm, axis=0) == 0).all()
    assert (np.max(norm, axis=0) == 1.0).all()


def normalize(arr):
    mins = np.min(arr, axis=0)
    maxs = np.max(arr, axis=0)
    return (arr - mins) / (maxs - mins)


def test_standardizer():
    data = np.random.uniform(size=20).reshape((10, 2)) * 100
    standardized = standardizer(data)
    np.testing.assert_array_less(np.mean(standardized, axis=0), 1e-14)
    np.testing.assert_allclose(np.var(standardized, axis=0), 1)


def standardizer(x):
    means = np.mean(x, axis=0, keepdims=True)
    stds = np.std(x, axis=0, keepdims=True)
    return (x - means) / stds
