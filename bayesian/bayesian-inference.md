## Motivations

What's wrong with black box ML
- opaque interface to the full model
- constrained models
- no uncertainty

Probabilistic
- clear inference
- extreme flexibility
- useful - can make complex models from simple components
- full uncertainty
- philsophically interesting
- generate data

### Narrative

> More generally, Cronin writes:[1] Probabilistic programming will unlock narrative explanations of data, one of the holy grails of business analytics and the unsung hero of scientific persuasion. People think in terms of stories—thus the unreasonable power of the anecdote to drive decision-making, well-founded or not. But existing analytics largely fails to provide this kind of story; instead, numbers seemingly appear out of thin air, with little of the causal context that humans prefer when weighing their options.Davidson-Pilon, Cameron. 
>
Bayesian Methods for Hackers (Addison-Wesley Data & Analytics Series) (pp. 34-35). Pearson Education. Kindle Edition. 
 
### Probabilistic programming

Probabilistic programming
- write a program that can generate data like your data
- automatic inference for unknown parameters

## Bayesian methods

Freq vs Bayes = question of philsophy - definition of probability

freq = freq of repeated events
- analyze data in terms of fixed model params
- varying data, fixed model

Bayes = our own uncertainty about an event
- variation of beliefs about parameters in terms of fixed dat
- fixed data, varying model

Simple problems - freq + bayes = the same

differences become apparent in more complex
- nuisance params, interpreting uncertainty, incorporatnig priors, comparing & evaluating models

Bayesian = updating beliefs

Bayesian probability = belief
- contrasted with frequentist probability
- both are correct

$P(A)$ = prior

$P(A|X)$ = posterior

$P(X)$ = model evidence / data

Model evidence = simply a normalization (only interesting in some situations)

Function we want = the posterior

Bayesian methodology will return a distribution

PYMC = Bayesian Probabilistic programming

## Bayes Theorem

$P(A|X) = \frac{P(X|A)P(A)}{P(X)}$

Allows using new data without retraining

Connects the posterior with the prior

Example
- 1/100 prob of disease
- test gives 1/110 ppl a positive result
- if you have the disease, prob of positive result = 65 / 100

$P(D|T) = P(T|D)P(D) / P(T) = (65/100 * 1/100)/(1/110) = 0.715$

### The normalizing constant

$P(X)$

PYMC = unormalized - don't need to calculate the normalizing constant

## The Bayesian modelling approach

1. what variables describe the data (what kind of distribution)
2. what do these distributions need (hyperparams)
3. do we know the hyperparams
4. what distributions describe the hyperparams

If we don't know, can use uniform

## Useful distributions

Poisson - expectation == parameter, 
Poisson for counts for all integers

Binomial
counts up until n integers

Bernoulli

Continuous = use exponential, expectation == 1 / parameter
