# Statistics

These notes are built using
- [Statistics Done Wrong - Alex Reinhart](https://www.statisticsdonewrong.com/)
- [Think Stats 2nd Edition - Allen B. Downey](https://greenteapress.com/wp/think-stats-2e/)
- [Practical Statistics for Data Scientists - Bruce & Bruce](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/)
- [Deep Learning - Goodfellow, Bengio and Courville](https://www.deeplearningbook.org/)
- [Statistics for Hackers - PyCon 2016 - Jake Vanderplas](https://www.youtube.com/watch?v=Iq9DzN6mvYA)
- [Visual Information Theory - colah's blog](https://colah.github.io/posts/2015-09-Visual-Information/)
- [Sutton & Barto - Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf)

I reccomend all the resources above and thank all the authors for their excellent contributions to the world.

## Course content

[intro.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/intro.ipynb)
- IID
- probability
- median versus mean
- ranking
- average versus marginal
- Simpson's paradox
- survivorship bias
- pseudoreplication

[distributions.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/distributions.ipynb)
- histograms
- probability mass functions
- cumulative distribution functions
- quantiles

[correlation.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/correlation.ipynb)
- covariance
- Pearson & Spearman correlation
- Anscombe's quartet

[estimation.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/estimation.ipynb)
- error in sampling
- sampling bias
- sampling error
- estimating sampling statistic distributions
 
[hypothesis-testing.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/hypothesis-testing.ipynb)
- p-values
- Chi-Squared tests
- statistical power 
- base rate fallacy
- multiple comparisons

[bandits.ipynb]
- reinforcement learning context
- exploration versus exploitation
- multi-armed bandit
- epsilon greedy
- upper confidence bound

[central-limit-theorem.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/central-limit-theorem.ipynb)
- why we can use Gaussians all the time

[complexity.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/complexity.ipynb)
- how code slows as data grows

[entropy.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/entropy.ipynb)
- information theory
- entropy
- cross-entropy
- Kullback-Leibler divergence
- softmax 

[answers.py](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/answers.py)
- for completeness
-` import answers`

[common.py](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/intro.ipynb)
- code shared between notebooks
- a best practice - often the result of a first refactor