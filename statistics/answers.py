import numpy as np
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