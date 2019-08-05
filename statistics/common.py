import numpy as np
import pandas as pd
from sklearn import datasets


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
    return features, target


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