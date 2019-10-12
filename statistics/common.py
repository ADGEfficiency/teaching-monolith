from collections import namedtuple
import os

import numpy as np
import pandas as pd
import requests
from sklearn import datasets


Data = namedtuple('Data', ['features', 'target', 'target1D'])


def load_iris():
    dataset = datasets.load_iris()
    features = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    target = pd.DataFrame(pd.get_dummies(dataset.target))
    target.columns = dataset.target_names
    assert features.shape[0] == target.shape[0]
    print('The Iris dataset was used in R.A. Fisher\'s classic 1936 paper *The Use of Multiple Measurements in Taxonomic Problems*.')
    print('')
    print('features.shape = {}'.format(features.shape))
    print('target.shape = {}'.format(target.shape))
    return Data(features, target, pd.DataFrame(dataset.target, columns=['class']))

def load_forest_fires():
    os.makedirs('./data', exist_ok=True)

    files = ['forestfires.csv']
    print('Downloading forest fires dataset - the aim is to predict the burned area of forest fires, in the northeast region of Portugal, by using meteorological and other data')
    for name in files:
        res = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/{}'.format(name))
        with open('./data/{}'.format(name) , 'wb') as f:
            f.write(res.content)
    data = pd.read_csv('./data/forestfires.csv')
    
    print('')
    print('data.shape = {}'.format(data.shape))
    print('columns {}'.format(list(data.columns)))
    return data


def make_pmf(samples):
    uniq, counts = np.unique(samples, return_counts=True)
    pmf = counts / np.sum(counts, axis=0)
    return uniq, pmf


def percentile_rank(value, samples):
    count = 0
    return sum([count + 1 for s in samples if s <= value]) / len(samples)


def percentile(rank, samples):
    samples = sorted(samples)
    idx = int(rank * (len(samples) - 1))
    return samples[idx]


def make_cdf(samples):
    samples = sorted(samples)
    return [(percentile_rank(s, samples), s) for s in sorted(samples)]