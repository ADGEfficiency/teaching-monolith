import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import entropy as entropy_from_probs


def central_limit():
    num_plots = 12
    nrows = 3
    epochs = 5000

    freq = int(epochs / num_plots)

    def sample_means(iters=100):
        return [
            np.mean(pop[np.random.randint(0, pop.shape[0], size=100)])
            for _ in range(iters)
        ]

    pop = np.random.uniform(0, 100, size=10000)

    f, axes = plt.subplots(ncols=int(num_plots/nrows), nrows=nrows, figsize=(25, 10))
    means = []
    for num, ax in enumerate(axes.flatten()):  
        me = sample_means(freq)

        s = []
        for de in me:
            if de > 50.0 and np.random.rand() > 0.5:
                means.append(de)

        pd.DataFrame(means).plot(ax=ax, kind='hist', legend=None, title=num*freq)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)


def distributions():
    name = 'temp'
    data = raw.loc[:, name]

    f = plt.hist(data)
    _ = plt.ylabel('frequency')
    _ = plt.xlabel(name)
    
    percentile(0.25, data)
    percentile(0.75, data)
    
    rank = percentile_rank(10, data)
    percentile(rank, raw.loc[:, 'wind'])

    
def entropy_from_classes(y):
    probs = [sum(y == i) / len(y) for i in set(y)]
    np.testing.assert_allclose(sum(probs), 1)
    return entropy_from_probs(probs)


def expectation(results):
    return {arm: np.mean(data) for arm, data in results.items()}


def cross_entropy_from_probs(p, q):
    epsilon = 1e-16
    return sum([-tr * math.log(est + epsilon, 2) for tr, est in zip(p, q)])


def ucb(results, step, c):
    return {
        arm: np.mean(data)+ c * np.sqrt(np.log(step)/len(data))
        for arm, data in results.items()
    }


def run_ucb_expt(c=5):

    results = {
        arm: list(np.random.normal(*stats))
        for arm, stats in params.items()
    }

    steps = 1000
    values = np.zeros((steps, len(choices)))
    actions = np.empty((steps)).astype(str)
    ucb_performance = np.zeros(steps)

    for step in range(steps):
        ucbs = ucb(results, 2, c)

        action = max(ucbs, key=ucbs.get)
        actions[step] = action
        values[step, :] = list(ucbs.values())

        p = params[action]
        results[action].append(float(np.random.normal(p.loc, p.scale, 1)))
        ucb_performance[step] = get_performance(results)
        
    return ucb_performance