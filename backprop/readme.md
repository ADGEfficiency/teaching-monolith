## Lecture

Backpropagation is introduced in the [intro-to-backprop notebook](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/intro-to-backprop.ipynb).

During the lecture you will start to get an appreciation of hyperparameters used in neural networks
- learning rate - used to scale the magnitude of the gradient update
- batch size - the number of samples used to calculate gradients
- weight initialization
- choice of loss function
- why gradient clipping & standardization is a best practice

## Practical

Examples of numpy neural networks are given in the [classification](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/classification.ipynb) and [regression](https://github.com/ADGEfficiency/teaching-monolith/blob/master/backprop/regression.ipynb) notebooks for single hidden layer neural networks.

The practical for this class is to:
- extend the neural nets to two hidden layers
- extend the neural nets to n hidden layers
- implement SGD (batching)
- optimize the training (learning rate decay, early stopping etc)
- gradient clipping

## Resources & further reading

[Tensorflow Neural Network Playground](https://playground.tensorflow.org/)

## Backprop theory

[Calculus on Computational Graphs: Backpropagation](http://colah.github.io/posts/2015-08-Backprop/)

[CS231n - Backprop](http://cs231n.github.io/optimization-2/)

## Classification neural net from scratch

[dennybritz/nn-from-scratch](https://github.com/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb)

[Understanding softmax and the negative log-likelihood](https://ljvmiranda921.github.io/notebook/2017/08/13/softmax-and-the-negative-log-likelihood/
)
