[alexeygrigorev/data-science-interviews ](https://github.com/alexeygrigorev/data-science-interviews) - data science interview questions with answers

## p-values

If you perform a statistical test and get a p-value of 0.01.

Based on this, decide whether each of the following statements is true or false: 

- you have absolutely disproved the null hypothesis (“There is no difference between means”). 
- there is a 1% probability that the null hypothesis is true. 
- you have absolutely proved the alternative hypothesis (“There is a difference between means”). 
- you can deduce the probability that the alternative hypothesis is true. 
- you know, if you decide to reject the null hypothesis, the probability that you are making the wrong decision. 
- you have a reliable experimental finding, in the sense that if your experiment were repeated many times, you would obtain a significant result in 99% of trials.

# Questions

## Generic

Where ALGO can be
- SVM
- random forest
- gradient boosted trees

Explain ALGO machine learning algorithm in detail 

Is ALGO parametric or non-parametric?


## SVM

What are support vectors in SVM?

What are the different kernel functions in SVM?


---

What is your favourite loss function?

What is the difference between supervised and unsupervised machine learning?

What is bias, variance trade off?

What are exploding gradients?

What is a confusion matrix?

Explain how a ROC curve works.

Explain L1 and L2 regularisation.

What is selection bias?
- aka sampling bias = samples having different probabilities than others
- non iid


Explain decision tree algorithm in detail.

What is entropy and information gain in a decision tree algorithm?

What is pruning in a decision tree?

What is ensemble learning?

What is a random forest? How does it work?

What cross-validation technique would you use on a time series data set?

What is logistic regression? 

State an example when you have used logistic regression recently.

What do you understand by the term normal distribution?

What is a Box-Cox Transformation?

How will you define the number of clusters in a clustering algorithm?

What is deep learning?

What are recurrent neural networks (RNNs)?

What is the difference between machine learning and deep learning?

What is reinforcement learning?

Explain what regularisation is and why is it useful.

What is TF/IDF vectorization?

What are recommender systems?

What is the difference between regression and classification?

regression metrics
- 

how PCA works
- saving compute
- removes noise -> reduces variance
- wouldn't use of your features are from very different sources

L1 vs L2 regularization

How to deal with imbalanced classes

How to deal with missing values
- drop rows
- drop columns
- fill in with simple stats
- use another model to predict

what would you do with a multi modal target

feature importances

## shorter form questions

---

Linear independence

Determinant

Eigenvalues and Eigenvectors

SVD

The norm of a vector

Independent random variables

Expectation and variance


Entropy, what it means intuitively, formula

KL divergence, other divergences

Kolmogorov complexity

Jacobian and Hessian

Gradient descent and SGD

Other optimization methods

NN with 1k params - what’s dimensionality of a gradient and hessian

What is SVM, linear vs non-linear SVM

Quadratic optimization

NN overfits - what to do

What is autoencoder

How to train an RNN

Favorite ML algorithm - tell about it in details


---

Coding
Fizzbuzz
Given a list of timestamps in sequential order, return a list of lists grouped by weekly aggregation.
Given a list of characters, a list of prior of probabilities for each character, and a matrix of probabilities for each character combination, return the optimal sequence for the highest probability.
Given a log file with rows featuring a date, a number, and then a string of names, parse the log file and return the count of unique names aggregated by month.
Product
Given there are no metrics being tracked for Google Docs, a product manager comes to you and asks what are the top five metrics you would implement?
In addition, let’s say theres a dip in the engagement metric of Google Docs. What would you investigate?
Let’s say we want to implement a notification system for reminding nurses to discharge patients at a hospital. How would you implement it?
Let’s say at LinkedIn we want to implement a green dot for an “active user” on the new messaging platform. How would you analyze the effectiveness of it for roll out?
SQL
Given a payment transactions table and a customers table, return the customer’s name and the first transaction that the customer made.
Given a payments transactions table, return a frequency distribution of the number of payments each customer made. (I.E. 1 transaction — 100 customers, 2 transactions — 50 customers, etc…)
Given the same payments table, return the cumulative distribution. (At least one transaction, at least two transactions, etc…)
Given a table of — friend1|friend2. Return the number of mutual friends between two friends.
AB Testing
Given AB test funnel statistics such as the sample size, sign up rate, feature 1 usage rate, feature 2 usage rate, analyze which variant won and why.
How would you design an experiment to change a button on a sign up page?
How do you know if you have enough sample size?
How do you run significance tests on more than one variant?
How do you reduce variance and bias in an AB test?
Explain a P-value and confidence interval to a product manager or non-technical person.
Machine Learning
What features would you use to predict the time spent for a restaurant preparing food from the moment an order comes in?
Can you come up with a scenario in which you would rather under-predict versus over-predict?
Analyzing the results of a model, how would you explain the tradeoff between bias and variance?
Explain how a Random Forest model actual works under the hood.
How do you know if you have enough data for your model?
How do you evaluate a model? (F1 score, ROC curve, cross validation, etc…)
Probability
Given uniform distributions X and Y and the mean 0 and standard deviation 1 for both, what’s the probability of 2X > Y?
There are four people in an elevator and four floors in a building. What’s the probability that each person gets off on a different floor?
What’s the probability that two people get off on the same floor?
Given a deck of cards labeled from 1 to 100, what’s the probability of getting Pick 1 < Pick2 < Pick3?

## Five Interview Questions to Predict a Good Data Scientist - [medium](https://medium.com/predict/five-interview-questions-to-predict-a-good-data-scientist-40d310cdcd68)

Significance of the normal distribution
- Central Limit Theorem
- mean, medium and mode are all the same
- entire distribution can be specified by two paraemters (mean and variance)
- importance for linear regression

---

what is linear regression

what is overfitting

what is the ROC curve

what is rf

rf vs boosting
