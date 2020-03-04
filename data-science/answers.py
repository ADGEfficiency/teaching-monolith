import numpy as np
from sklearn.ensemble import RandomForestRegressor


def stability_selection_rf_regressor(x, y, params, depths, straps=4, k=5):
    rows, cols = x.shape
    regs = depths
    scores = np.zeros((cols, depths.shape[0]))
    for idx, reg in enumerate(regs.flatten()):

        bootstrap_features = np.zeros((cols, straps))
        for strap in range(straps):
            sample = np.random.choice(np.arange(rows), size=rows//2, replace=False)

            x_tr = x.values[sample, :]
            y_tr = y.values[sample]
            params['max_depth'] = reg
            model = RandomForestRegressor(**params)
            model.fit(x_tr, y_tr)

            impts = model.feature_importances_
            bootstrap_features[:, strap] = (impts > np.mean(impts)).astype(int)

        scores[:, idx] = np.mean(bootstrap_features, axis=1)

    feature_scores = np.mean(scores, axis=1).flatten()
    feature_scores.shape[0] == x.shape[1]
    best = feature_scores.argsort()[-k:][::-1]
    return x.columns[best]