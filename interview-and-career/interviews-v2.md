## Regression with tree based ensembles

What is bias, variance, capacity

```
- bias = different between expected & true
- variance = variability of prediction
- capacity = ability for model to understand cowplex relationships between variables
```

RF vs XGB 

What is cross validation?
- why
- when not to use it

R2 as a metric
- variance explained by the regression / total variance
- the more predictors you add the higher R^2 becomes.  hence use adjusted R^2 which adjusts for the degrees of freedom 

BONUS
-mse = variance + bias squared
- relative importance / infomation gain

bagging
- averages out enstable learning algorithms

boosting
- reweights examples near the decision edge (the margin)

## Binary classification with logistic regression

Explain how logistic regression works

Why do we use a sigmoid
- why not tanh or relu?

Use an example to show the drawback of accuracy as a metric

Business problem where we want precision, recall

What is a confusion matrix?

What is the F1 score, ROC curve

What is 'threshold tuning'?

How to deal with imbalanced classes

How to regularize?


## A/B testing



## Basic stats & prob

normal dist
- mean == mode == median

Significance of the normal distribution
- Central Limit Theorem
- mean, medium and mode are all the same
- entire distribution can be specified by two paraemters (mean and variance)
- importance for linear regression

what is standard normal
- mean=0, std=1

what is IQR
- interquartile range
- 25 vs 75 percentiles

parametric or non-parametric
- lasso
- svm
- rf
- ff
- conv
- lstm

Central limit theorem
