import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)

    sources = sorted(df['source'].unique())
    targets = sorted(df['target'].unique())
    rating_matrix = pd.DataFrame(index=sources, columns=targets)

    rating_matrix = rating_matrix.fillna(0)
    rating_pivot = df.pivot(index='source', columns='target', values='rating').fillna(0)
    rating_matrix.update(rating_pivot)
    
    rating_ndarray = rating_matrix.to_numpy(dtype=np.float32)
    return rating_ndarray


def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    
    sources = sorted(df['source'].unique())
    targets = sorted(df['target'].unique())
    
    frequent_matrix = pd.DataFrame(index=sources, columns=targets)
    
    frequent_matrix = frequent_matrix.fillna(0)
    freq_counts = df.groupby(['source', 'target']).size().unstack(fill_value=0)

    frequent_matrix.update(freq_counts)
    frequent_ndarray = frequent_matrix.to_numpy(dtype=np.float32)
    return frequent_ndarray
