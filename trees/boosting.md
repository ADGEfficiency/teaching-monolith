# Boosting

Boosting = learning models in series (sequentially) to minimize error of previous models

There are a few variants
- AdaBoost (1995)
- gradient boosting
- stochastic gradient boosting (using samples without replacement for each tree)


## Example - teacher journey home length

Your teacher estimates their travel time home by looking at the weather.  A student has access the data they don't (from Google Maps).  The student predicts the teacher will be 5 minutes slower

The combination of these two prediction is the prediction of a gradient boosted ensemble of two people as base learners (equivalent to trees) using data from the weather and Google Maps (the features).


## Gradient boosted trees

XGBoost + feature engineering = most Kaggle winners

Next tree trained to improve the already trained ensemble by **predicting the residuals**
- prediction is the sum of all trees (weighted by a learning rate)
- sequential learning
- high bias, low variance base learners

In boosting, trees are grown sequentially
- each tree is grown to correct the mistakes of previous trees

GBM = optimizes an objective function - including ranking and poission regression (this is harder with RF)

Optimization occurs in function (not parameter) space
- gradient descent with functions

**Learn slowly**
- fit decision tree to the residuals of the current model
- we use the residuals (rather than Y) as the target
- add this new decision tree into the fitted function in order to update the residuals

Trees can be small, with just a few terminal nodes
- by fitting small trees, we slowly improve in areas where it doesn't perform well

Can work with weird loss functions
- can handle constant gradients
- quantile (pinball) loss


## Gradient descent with functions

Both are
- iterative
- minimize a loss

The gradients are the residuals!
- fit each base learner to the -ve gradient of the loss function from the previous iteration

Gradient descent = follow negative gradients to choose parameter updates
- descend by changing parameters

Gradient boosting = choose a function that points in negative gradient direction 
- descend by introducing new models

Misleading to think of gradient boosting as fitting residuals (or even pseudo residuals as the gradients are often named), it is actually gradient descent in function space.


## Implementations

- [XGBoost](https://xgboost.readthedocs.io/) - start here
- [CatBoost](https://catboost.ai/) 
- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)


## Boosting hyperparameters

Based on the [XGBoost documentation](https://xgboost.readthedocs.io/en/latest/python/python_api.html)

Other implementation docs

- [sklearn GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)

`n_estimators`
- number of boosting steps

`max_depth`
- control variance

`learning_rate`
- controls how trees are added together
- controls variance
- smaller for noisy data

`subsample`
- controls how random the data each base learner trains on is
- sampling without replacement
- control variance

`alpha`
- Manhattan distance
- L1 regularization

`lambda`
- squared Euclidean distance
- L2 regularization

`gamma`
- loss reduction threshold for making partition on a tree


## Starting point hyperparameters

Heard from a Kaggle Grandmaster

Learning rate = 0.05, 1000 rounds, max depth = 3-5, subsample = 0.8-1.0, colsample_bytree = 0.3 - 0.8, lambda = 0 to 5

Add capacity to combat bias - add rounds

Reduce capacity to combat variance - depth / regularization

```json
{'colsample_bytree': 0.7978421458577196, 'lambd': 2.5982975135904516, 'max_depth': 4, 'subsample': 0.8913639174845348, 'n_estimators': 500}
```

## How can sequential learning be parallelized?

Parallelization within a single tree
- create branches independently
