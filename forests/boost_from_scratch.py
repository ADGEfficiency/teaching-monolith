import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor


if __name__ == '__main__':
    #  simple dataset
    x = np.random.uniform(0, 100, 10000).reshape(-1, 1)
    y = np.sin(x).ravel()
    assert x.shape[0] == y.shape[0]
    assert len(y.shape) == 1

    bootstrap_size = 1000
    rounds = 5

    preds = np.zeros((rounds, bootstrap_size))

    for rnd in range(rounds):
        idxs = np.random.randint(0, bootstrap_size, bootstrap_size)

        tree = DecisionTreeRegressor()

        #  use all features
        feature_idx = np.arange(x.shape[1])
        batch = x[idxs, feature_idx].reshape(-1, x.shape[1]), y[idxs]

        tree.fit(*batch)

        pred = tree.predict(batch[0])
        error = np.mean(pred - batch[1])
        print(np.sum(error))
        preds[rnd, :] = pred

        #  learning rate goes here
        y = pred - batch[1]

    f, a = plt.subplots()
    plt.plot(np.mean(preds, axis=1))
    plt.savefig('./out.png')
