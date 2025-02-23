---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region -->
# Backpropagation

## What's So Important About Backprop

Backprop is a cross-disciplinary computational tool, that been discovered and rediscovered many times.

From [The Master Algorithm](https://en.wikipedia.org/wiki/The_Master_Algorithm):

> In fact, Rumelhart is credited with inventing backprop by the Columbus test: Columbus was not the first person to discover America, but the last.
>
> It turns out that Paul Werbos, a graduate student at Harvard, had proposed a similar algorithm in his PhD thesis in 1974. And in a supreme irony, Arthur Bryson and Yu-Chi Ho, two control theorists, had done the same even earlier: in 1969, the same year that Minsky and Papert published Perceptrons!


**It speeds up training of neural networks**.  Alternatives include computing the directional derivatives via finite difference (which would mean doing millions of forward passes).

## What is Backprop

Backprop is a mathematical technique for quickly calculating derivatives.

It's the application of *reverse-mode differentiation* (the application independent name for backprop) to neural networks.

Backpropagation is not a training algorithm:

- it’s an algorithm for computing the gradient,
- gradient descent is the training algorithm.

Backpropagation involves two steps:

1. a forward pass from `data -> input layer -> output layer -> prediction error`,
2. a backwards pass from `prediction error -> gradients -> output layer -> input_layer`.

The error from the forward pass is backpropagated from the output layer back through the network - updating the weights in reverse order.

From [The Master Algorithm](https://en.wikipedia.org/wiki/The_Master_Algorithm):

> With backprop, you don’t have to figure out how to tweak each neuron’s weights from scratch, which would be too slow; you can do it layer by layer, tweaking each neuron based on how you tweaked the neurons it connects to.

From [The Singularity Is Near](https://en.wikipedia.org/wiki/The_Singularity_Is_Near):

> However, backpropagation is not a feasible model of training synaptic weights in an actual biological neural network, because backward connections to actually adjust the strength of the synaptic connections do not appear to exist in mammalian brains.
>
> In computers, however, this type of self-organizing system can solve a wide range of pattern-recognition problems, and the power of this simple model of self-organizing interconnected neurons has been demonstrated.

## Gradients

The gradient is both a direction and a rate of change. Both of these are valuable:

- the direction can be the direction that reduces error,
- the rate of change can be the largest (steepest) rate of change to reduce error.

The change is always in the context of something else.  For neural networks, we are interested in how **error changes with respect to our parameters**.

## Calculus 101

Calculus is the study of change.  Below we introduce just enough calculus fundamentals to understand the chain rule and backpropagation.

If I have a function:

$$ f(x) = x^2 $$

The algorithm to find the derivative is known as the **Power Law**:

1. multiply by the power,
2. subtract the power by one.

$$ f'(x) = 2x $$

$$ f(x) = 3x^4 + 2x^{2} $$
$$ f'(x) = 12x^3 + 4x $$

$$ f(x) = 8x $$
$$ f'(x) = 8 $$

If I take the derivaitve with respect to $x$ on something that doesn't depend on $x$, then the derivative is zero.  This includes:

- constants $10, -1$,
- terms that don't have an $x$ such as $y^2, \theta$.

$$ f(x) = 2x + 5y + 8 $$
$$ f'(x) = 2 $$

If I have something in brackets raised to a power, then the derivative is the power times the bracket to the power minus one, times the derivative of what is in the bracket:

$$ f(x) = g(x)^3 $$
$$ f'(x) = 3 g(x)^2 \cdot g'(x) $$

$$ f(x) = (x^2 + x)^3 $$
$$ f' = 3(x^2 + x)^2 \cdot (2x + 1) $$

We use this rule to take the derivative of the mean square error.

## Notation

Calculus was discovered by multiple people around the same time - this has led to a number of competing notations:

$$ \nabla_{x} f = f' = \frac{df}{dx} $$

## Minimizing a Function

Our use case of calculus is to find the minimum of a function - to find the minimum of our loss function.

To find the minimum of a simple function:

$$ f(x) = x^2 $$

We can **sample data** from this function.  From the data below it is clear where the minimum is (but lets pretend it isn't):

| x  | f(x) |
|----|------|
| -5 | 25   |
| -2 | 4    |
| 0  | 0    |
| 2  | 4    |
| 5  | 25   |

We can take the derivative of this function, and it shows us the direction we need to take to find the minimum:

$$ f'(x) = \frac{df}{dx} = 2x $$

| x  | f(x) | f'(x) |
|----|------|-------|
| -5 | 25   | -10   |
| -2 | 4    | -4    |
| 0  | 0    | 0     |
| 2  | 4    | 4     |
| 5  | 25   | 10    |

This shows us the value of a gradient - it shows us the direction towards maximizing a function (we take the negative to minimize it).

Gradient descent is an iterative process that repeatedly takes steps in the direction of the negative gradient.

## Fitting a Function

The example above shows how we can use gradients to find the minimum of a function.

In machine learning, the function we want to minimise is an **error or loss function**.

This error is the difference between two functions:

- a function that we parametrize $f(x; \theta)$ with weights $\theta$,
- a function that we want to learn $F(x)$.

We don't have access to $F(x)$ (if we did, we wouldn't need to learn it) - what we do have access to is the ability to sample:

- $x$ - features (inputs),
- $y$ - target / label (outputs).

We have three things:

1. a function parametrized by weights $\theta$
2. samples of $x$ (features)
3. samples $y$ (target)

Lets learn from data sampled from the function:

$$F(x) = 3 x^2 $$

This is a parameterized function with a single feature:

$$ f(x; \theta) = \theta x^2 $$

Samples:

| x  | y  |
|----|----|
| -1 | 3 |
| 0  | 0  |
| 1  | 3  |

Mean square error:

$$E = \frac{1}{2} (f(x; \theta) - y)^2 = \frac{1}{2} (\theta x^2  - y)^2 $$

Derivative of the error:

$$E' = \frac{dE}{d\theta} = (\theta x^2 - y) \cdot x^2 $$

We can now perform an iterative process to update our parameter $\theta$, starting from an initial $\theta = 0 $:

| x  | y  | E' |
|----|----|----|
| -1 | 3 |  -6 |
| 0  | 0  | 0  |
| 1  | 3  | -6 |

How do we update our parameter? One way is to average over the three samples:

$$E' = (-6 + 0 -6) / 3 = -4.0$$

As we are minimizing the error, we take the negative of the gradient and use it to update our parameter:

learning rate
alpha = 0.1
$$\theta_{1} = \theta_{0} + E' = 0 + 0.1 * 4 = 0.4 $$

Which is not so far away from the true value of $3$.

Here we are seeing the need for two of the most important hyperparameters in training neural networks - the **learning rate** & **batch size**. Can you see how they would fit into our example?

## Practical

Do this (on paper!) for $f(x) = 5 x^3$

## Partial Derivatives

In the example above we used our prior knowledge of the true function $F(x)$ to engineer a single feature $x^2$.

What happens if we don't encode this knowledge, and instead have multiple parameters?

$$ f(x;\theta) = \theta_{0} x^2 + \theta_{1} x + \theta_{2} $$

We now need partial derivatives:

$$ \frac{\partial f}{\partial \theta_{0}} = x^2 $$

$$ \frac{\partial f}{\partial \theta_{1}} = x $$

$$ \frac{\partial f}{\partial \theta_{2}} = 1 $$

## Practical

Lets pick some initial parameters (this is **weight initialization**):

$$\theta = [1,1,1]$$

Calculate the partial derivatives and update the parameters using the following data:

| x  | y  |
|----|----|
| -2 | -5 |
| 0  | 1  |
| 1  | 4  |

## The Linear Perceptron

If we have a feature of length 3:

$$x = [x_{0}, x_{1}, x_{2}]$$

Let give each feature its own parameter:

$$ \theta = [\theta_{0}, \theta_{1}, \theta_{2}] $$

And combine them together using a linear combination:

$$ f(x; \theta) = x_{0} \cdot \theta_{0} + x_{1} \cdot \theta_{1} + x_{2} \cdot \theta_{2} $$

$$ f(x; \theta) = \sum x \cdot \theta $$

## The Perceptron

From [The Singularity Is Near](https://en.wikipedia.org/wiki/The_Singularity_Is_Near):

> This basic neural-net model has a neural “weight” (representing the “strength” of the connection) for each synapse and a nonlinearity (firing threshold) in the neuron soma (cell body).

This linear combination won't be much use for learning a non-linear function.  Let's adjust notation in anticipation of complexity:

$$ z(x) = \sum x \theta $$

Lets add an activation function after the linear combination - lets use a sigmoid (which is a special case of the logistic function):

$$ a(z) = \frac{1}{1 + e^{-z}} $$
<!-- #endregion -->

## A Single Hidden Layer Neural Network

Three layers in total - input, hidden & output.

Parameters from input -> hidden layer:

$$w_{0}, b_{0}$$

Linear combination of parameters:

$$z_{0} = \sum X \cdot w_{0} + b_{0}$$

Hidden layer activation function (sigmoid):

$$a_{0} = \frac{1}{1 + \exp^{-z}} $$

Output layer linear combination:

$$z_{1} = \sum a_{0} \cdot w_{1} + b_{1}$$

Error function:

$$E = \frac{1}{2} (z_{1} - y)^2$$

## Partial Derivatives of These Components

Partial derivative of the linear combination of the input layer with respect to a weight or bias in that layer:

$$ \frac{\partial z_{0}}{\partial  w_{0}} = X $$

$$ \frac{\partial z_{0}}{\partial  b_{0}} = 1 $$

Partial derivative of the sigmoid activation on the hidden layer with respect to the linear combination:

$$ \frac{\partial a_{0}}{\partial  z_{0}} = a_{0}(z_{0}) * (1-a_{0}(z_{0})) $$

Partial derivative of the output layer linear combination with respect to the activation:

$$ \frac{\partial z_{1}}{\partial a_{0}} = w_{1} $$

Partial derivative of the error with respect to the output layer:

$$ \frac{\partial E}{\partial z_{1}} = z_{1} - y $$

Our full model can now be written as a composition of functions:

$$ f(x; \theta) = z_{1}(a_{0}(z_{0}(x))) $$

We want change each of our parameters with respect to minimize the error:

$$ \frac{\partial E}{\partial w_{0}}, \frac{\partial E}{\partial b_{0}}, \frac{\partial E}{\partial w_{1}}, \frac{\partial E}{\partial b_{1}} $$

## The Chain Rule

When we have compositions of functions:

$$ f(x) = a(z(x)) $$

The **chain rule** shows us how gradients flow through these compositions of functions:

$$ \frac{df}{dz} = \frac{df}{da} \cdot \frac{da}{dz} $$

## Practical

You now have all the tools to derive update equations for all our weights and biases - do so on paper.

```python

```
