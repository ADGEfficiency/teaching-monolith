# Backpropagation

## Lecture

Backpropagation is introduced in [intro-to-backprop](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/intro-to-backprop.ipynb), which introduces calculus, the chain rule and backpropagation.

This will give you an appreciation of hyperparameters used in neural networks:

- **learning rate** - used to scale the magnitude of the gradient update,
- **batch size** - the number of samples used to calculate gradients,
- **weight initialization**,
- choice of **loss function**,
- why **gradient clipping** & **standardization** is a best practice.

There is also a small notebook covering [dot-products](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/dot-products.ipynb).

## Practical

Neural networks built entirely from scratch in `numpy` are given in the [classification](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/classification.ipynb) and [regression](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/regression.ipynb) notebooks.

The practical for this class is to:

- extend the neural nets to two hidden layers,
- extend the neural nets to n hidden layers,
- implement SGD (batching),
- optimize the training (learning rate decay, early stopping etc),
- gradient clipping.

## Resources & Further Reading

[Tensorflow Neural Network Playground](https://playground.tensorflow.org/)

[Yes you should understand backprop - Andrej Karpathy](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b)

[Calculus: Early Transcendentals: Stewart, James, Clegg, Daniel K., Watson, Saleem](https://www.amazon.com/Calculus-Early-Transcendentals-James-Stewart-dp-1337613924/dp/1337613924/ref=dp_ob_title_bk)

[Calculus Made Easy: Thompson, Silvanus P., Gardner, Martin](https://www.amazon.com/gp/product/0312185480/ref=as_li_tl?camp=1789&creative=9325&creativeASIN=0312185480&ie=UTF8&linkCode=as2&linkId=f77fd8a70b9c53d8f82f48dfe7574a27&tag=susanfowler-20)

[Robert Ghrist course on multivariable calculus](https://www2.math.upenn.edu/~ghrist/)

## Backprop theory

[Calculus on Computational Graphs: Backpropagation](http://colah.github.io/posts/2015-08-Backprop/)

[CS231n - Backprop](http://cs231n.github.io/optimization-2/)

[Derivatives, Backpropagation, and Vectorization - Justin Johnson - 2017](http://cs231n.stanford.edu/handouts/derivatives.pdf)

## Classification neural net from scratch

[dennybritz/nn-from-scratch](https://github.com/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb)

[Understanding softmax and the negative log-likelihood](https://ljvmiranda921.github.io/notebook/2017/08/13/softmax-and-the-negative-log-likelihood/
)
