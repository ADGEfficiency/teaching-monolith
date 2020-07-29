import numpy as np
from scipy.special import softmax


def dot_product_attention():
    # see https://stackoverflow.com/questions/48100954/why-does-tf-matmula-b-transpose-b-true-work-but-not-tf-matmula-tf-transpos
    # use the `scipy` softmax to be able to softmax over the last dimension
    # transpose the array in a way that we don't transpose the batch 
    scores = np.matmul(qry, np.transpose(key, (0, 2, 1)))
    dist = softmax(scores, axis=-1)
    out = np.matmul(dist, val)