import pandas as pd
import numpy as np


ds = pd.DataFrame([
    {'customers-category': 'A', 'contract-length': 10, 'location': 'us'},
    {'customers-category': 'A', 'contract-length': 9, 'location': 'us'},
    {'customers-category': 'A', 'contract-length': 9, 'location': 'us'},

    {'customers-category': 'B', 'contract-length': 20, 'location': 'nz'},
    {'customers-category': 'B', 'contract-length': 30, 'location': np.nan},
    {'customers-category': 'B', 'contract-length': 10, 'location': 'nz'},

    {'customers-category': 'C', 'contract-length': np.nan, 'location': 'nz'},
    {'customers-category': 'C', 'contract-length': 5, 'location': 'nz'},
    {'customers-category': 'C', 'contract-length': np.nan, 'location': 'us'},
    {'customers-category': np.nan, 'contract-length': 1, 'location': 'nz'},
    {'customers-category': 'C', 'contract-length': 100, 'location': 'nz'},
])