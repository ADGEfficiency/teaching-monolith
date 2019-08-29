# Statistics

These notes lean heavily on
- [Statistics Done Wrong - Alex Reinhart](https://www.statisticsdonewrong.com/)
- [Think Stats 2nd Edition - Allen B. Downey](https://greenteapress.com/wp/think-stats-2e/)
- [Deep Learning - Goodfellow, Bengio and Courville](https://www.deeplearningbook.org/)

## Course content

[intro.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/intro.ipynb)
- IID
- probability

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
- sample statistics
- sample error
- pseudoreplication
 
[hypothesis-testing.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/hypothesis-testing.ipynb)
- p-values
- Chi-Squared tests
- statistical power 
- base rate fallacy
- multiple comparisons

[central-limit-theorem.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/central-limit-theorem.ipynb)

[complexity.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/complexity.ipynb)

[entropy.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/entropy.ipynb)
- information theory
- entropy
- cross-entropy
- Kullback-Leibler divergence
- softmax 

[mental-models.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/statistics/mental-models.ipynb)
- median versus mean
- ranking
- average versus marginal
- Simpson's paradox
- survivorship bias

---
A conscious decision was made to refactor out common code into `common.py`, rather than duplicate function definitions between notebooks
- this hurts notebook readability
- but demonstrates a software engineering best practice 

