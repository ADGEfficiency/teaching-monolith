from collections import namedtuple
import sys

import pandas as pd
import numpy as np
from scipy.stats import entropy

sys.path.append('../statistics')
from common import load_iris

#  used when iterating over potential splits
CandidateSplit = namedtuple('Candidate', ['entropy', 'weight'])

#  used when iterating over features
BestSplit = namedtuple(
    'Best',
    ['feature', 'entropy', 'boundary', 'left', 'right']
)

#  a node in the decision tree
Node = namedtuple('Node', ['left', 'right', 'boundary', 'feature', 'num'])


def calc_entropy(y):
    probs = [sum(y == i) / len(y) for i in set(y)]
    np.testing.assert_allclose(sum(probs), 1)
    return entropy(probs)


def make_split(target):
    ents = []
    splits = range(1, target.shape[0])
    for split in splits:
        left, right = target[:split], target[split:]

        l = CandidateSplit(calc_entropy(left), len(left) / len(target))
        r = CandidateSplit(calc_entropy(right), len(right) / len(target))

        split_entropy = l.entropy * l.weight + r.entropy * r.weight
        ents.append(split_entropy)

    best = np.argmin(ents)
    entropy = ents[best]
    split = splits[best]

    return entropy, split


def split_dataset_on_feature(data, feature):
    sorted_data = data.sort_values(feature).reset_index(drop=True)
    ent, split = make_split(sorted_data.loc[:, 'class'])
    boundary = sorted_data.iloc[split, :].loc[feature]

    left = sorted_data.iloc[:split, :]
    right = sorted_data.iloc[split:, :]
    return BestSplit(feature, ent, boundary, left, right)


def get_best_split(data, features):
    if isinstance(features, str):
        features = [features]

    results = []
    for feature in features:
        results.append(split_dataset_on_feature(data, feature))

    sort = sorted(results, key=lambda tup: tup.entropy)
    best = sort[0]
    print(best.feature, best.boundary)
    return best


def train_decision_tree(data, features=None, node=0):
    node += 1
    if len(set(data.loc[:, 'class'])) == 1 or data.shape[0] < 5:
        return 'leaf'

    feature, ent, boundary, left, right = get_best_split(data, features)

    if len(set(left.loc[:, 'class'])) > 1:
        left_node = train_decision_tree(left, features, node)
    else:
        left_node = None

    if len(set(right.loc[:, 'class'])) > 1:
        right_node = train_decision_tree(right, features, node)
    else:
        right_node = None

    return Node(left_node, right_node, boundary, feature, node)

if __name__ == '__main__':
    data = load_iris()

    raw = pd.concat([data.features, data.target1D], axis=1)

    cols = raw.columns
    tree = train_decision_tree(raw, cols[:-1]) # -1 to not include the class :)
    print(tree)
