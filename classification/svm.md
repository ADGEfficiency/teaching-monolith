SVM parametric?
- non parametric (RBF kernel)
- parameters grow with size of the training set
- RBF kernel calculates the pairwise distances between training data

RF parametric?
- no pruning + split based on a size (if node has less than X data points) -> non-parametric

https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf
http://pyml.sourceforge.net/doc/howto.pdf
https://medium.com/@kushaldps1996/a-complete-guide-to-support-vector-machines-svms-501e71aec19e
https://towardsdatascience.com/svm-implementation-from-scratch-python-2db2fc52e5c2
https://towardsdatascience.com/algorithms-from-scratch-support-vector-machine-6f5eb72fce10
https://medium.com/@fordcombs/svm-from-scratch-step-by-step-in-python-f1e2d5b9c5be
https://github.com/adityajn105/SVM-From-Scratch

[An Idiot’s guide to Support vector machines](https://web.mit.edu/6.034/wwwbob/svm-notes-long-08.pdf)

pre 1980 = linear

1980's = rf + neural nets (no theoretical basis)

1990's = efficient, non-linear

## Key ideas

Efficient separation of non-linear regions that use kernel functions

Generalization of similarity to measures based on dot-products

Optimization rather than greedy search


## Basic idea

Linearly separable patterns are easy (separated by a 'hyperplane')

This can be extended to non-linear separations by transforming data into a new space

- this transformation is done by a kernel function


## Support vectors

Hyperplane = decision surface

Support vector = data that lies closest to the hyperplane

- this data is hardest to classify
- this data determines location of the hyperplane


## Hyperplanes

There can be many ways to split data

- SVM will find the 'optimal' solution
- done by maximizing the margin

Maximizing the margin is a quadratic programming problem

- can be solved closed form
- reduce all weights to zero except a few that matter
- the non-zero weights are the support vectors

Hyperplane can be specified by a subset of the training data

- these are the support vectors
- removing support vectors would change the hyperplane position

Hyperplane defined by
$h_{1} = w \cdot x + b \geq 1$ when $y = 1$
$h_{2} = $w \cdot x + b \leq -1$ when $y = -1$

These can be combined

$ y(x \cdot w) \geq 1 $

$d$ = margin of separation

- distance between hyperplane and closest data point (for given W + b)

[details on the optimization - using Lagrangian to solve constrained optimization]


## Non-Linearity

Map data to high dimensional space to allow separation

Radial = polar co-ordinates

Kernel function = defines inner products (inner product == similarity) in the transformed space

- generalizes the notion of 'inner product similarity'
- replaces the dot product in the loss function

Common kernel functions

- polynomials
- radial basis functions (Gaussians)
- sigmoid


## Avoiding overfitting

Penalty function added for mistakes made after training


[The Complete Guide to Support Vector Machine (SVM)](https://towardsdatascience.com/the-complete-guide-to-support-vector-machine-svm-f1a820d8af0b)

Binary or multiclass

Optimal hyperplane = largest margin

Kernel 
- efficient way of making the non-linear boundary
- quantifies the similarity of two data points

[Support Vector Machines: A Guide for Beginners](https://www.quantstart.com/articles/Support-Vector-Machines-A-Guide-for-Beginners/)

Optimal = hyperplanes providing max distance

Memory efficient
- only store the support vectors

Flexible
- can use different kernels

Sensitive to support vector locations

Optimization = putting data on the correct side of the hyperplanes

- maximizing the distance

Use of a hyperparameter `C` allow slack variables
- to allow variables to be on the wrong side of the hyperplane
- controls margin violation
- controls the bias-variance tradeoff

Small `C` -> high variance, low bias

SVM uses non-linear kernels, by creating non-linear features with linear parameters
- non-linear in the original space
- linear in the transformed space

Kernel trick
- makes this computationally efficient
- only need inner product between observations

Classifier becomes a linear combination of inner products

Only need to calculate these inner products for the support vectors
- only the inner product between the observations
- not the observations themselves

Non-linear kernels replace how we calculate the similarity

Radial kernels
- localized behaviour
- only labels nearby have an impact on the class label

$\exp (- \gamma \sum (x_{ij} - x_{ji})^{2})$


## [1.4. Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)

Pros
- efficient in high dimensional spaces 
- effective when you have more features than samples (dense data)
- memory efficiency from only having to save the support vectors
- versatility from kernel functions

Cons
- no proability estimates

Multiclass classification = done using a 'one v one' approach
- train n_classes * (n_classes - 1) / 2 classifiers
- can then be transformed into a one versus rest classifier

Kernels
- linear
- polynomial
- rbf
- sigmoid

poly hyperparams
- `d` degree
- `r` intercept term

rbf hyperparams
- `C` controls variance
- `gamma` determines how much infulence a single sample has


## [A Practical Guide to Support Vector Classification](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf)

Minimize

$w^{T}w + C \sum \eta$ 

Subject to

$y (w^{T} \phi(x) + b) \ge 1 - \eta$

Kernel function = $\phi(x)^{T} phi(x)$

Sensitive to scale
- avoid large features dominiating small ones
- avoids problems with the inner product of feature vectors 


## [A User’s Guide to Support Vector Machines](http://pyml.sourceforge.net/doc/howto.pdf)

Kernel method = depends on the data only through dot-products
- dot product replaced by a kernel function
- avoid the explicit mapping of data to high dimensional space

Linear classifiers require the dot-product between data & weights

When $x^{T}x = 0$, then hyperplane that goes through the origin $b=0$

$y = w^{T}x + b = 0$ is the hyperplane, sign of $y$ determines which side of the plane a point is on


## Questions

Summarize the SVM
- map data to non-linear, high dimensional space to allow separation

Is the SVM parametric?
- linear = non parametric - determined only by the num features
- kernel = parametric - kernel matrix size depends on the size of the dataset

Is the SVM optimization closed or open form?
- closed, quadratic optimization

Why are SVM's memory efficient?
- only store the support vectors

How is the SVM flexible?
- use different kernels

What does the kernel trick let us do?  What does it allow us to avoid?
- replace dot-product with a kernel function
- defines the inner product in a high dimensional space
- avoid the mapping to a high dimensional space

What is a hyperplane?
- linear function
- line that separates classes

What is the maximal margin?

What is a soft margin?

What is a support vector?
- defines the hyperplane position

Is an SVM sensitive to normalization?  Why or why not?
1:
- SVM maximizes the distance between the hyperplane & support vectors
- if one feature has large values, it will dominate the distance calculation
2:
- kernel depends on inner products
- large values can cause numerical problems

What does the dot-product act like?
- similarity

How to reduce overfitting in an SVM?
- ie what does the parameter `C` do?
- determines the amount of slack variables that exist on the wrong side of the hyperplane

In the polynomial kernel, what do `d` and `r` do?
- `d` = degree
- `r` = intercept

In the RBF kernel, what does `gamma` do?
- determines the influence of distance

For kernel in [linear, polynomial, RBF, sigmoid]
- write the kernel

