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
    print("""For more information, read [Cortez and Morais, 2007].
        1. X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
        2. Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
        3. month - month of the year: 'jan' to 'dec'
        4. day - day of the week: 'mon' to 'sun'
        5. FFMC - FFMC index from the FWI system: 18.7 to 96.20
        6. DMC - DMC index from the FWI system: 1.1 to 291.3
        7. DC - DC index from the FWI system: 7.9 to 860.6
        8. ISI - ISI index from the FWI system: 0.0 to 56.10
        9. temp - temperature in Celsius degrees: 2.2 to 33.30
        10. RH - relative humidity in %: 15.0 to 100
        11. wind - wind speed in km/h: 0.40 to 9.40
        12. rain - outside rain in mm/m2 : 0.0 to 6.4
        13. area - the burned area of the forest (in ha): 0.00 to 1090.84
    (this output variable is very skewed towards 0.0, thus it may make
    sense to model with the logarithm transform).')""")
    for name in files:
        res = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/{}'.format(name))
        with open('./data/{}'.format(name) , 'wb') as f:
            f.write(res.content)
    data = pd.read_csv('./data/forestfires.csv')
    
    print('')
    print('data.shape = {}'.format(data.shape))
    print('columns {}'.format(list(data.columns)))
    return data


def dirty_forest():
    forest = load_forest_fires()

    dirty = forest.copy()

    for col in dirty:
        print(col)
        if dirty.loc[:, col].dtype == 'float64':
            mask = (np.random.rand(forest.shape[0]) > 0.98).astype(bool)
            dirty.loc[mask, col] += 2 * dirty.loc[:, col].std()

            mask = (np.random.rand(forest.shape[0]) > 0.98).astype(bool)
            dirty.loc[mask, col] -= 2 * dirty.loc[:, col].std()

    missing_mask = (np.random.rand(*forest.shape) > 0.95).astype(bool)

    dirty[missing_mask] = np.nan


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


def generate_bandit_dataset(arms=20, samples=2):
    np.random.seed(42)

    Param = namedtuple('Parameter', ['loc', 'scale', 'initial_size'])
    start = 10
    end = 50
    num_options = arms

    params = {
        str(option): Param(loc, scale, samples) 
        for option, (loc, scale) 
        in enumerate(zip(np.linspace(start, end, num_options), np.random.uniform(10, size=num_options)))
    }

    return params, {
        arm: list(np.random.normal(*stats))
        for arm, stats in params.items()
    }
