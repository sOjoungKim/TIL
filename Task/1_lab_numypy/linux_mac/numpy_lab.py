import numpy as np

def n_size_ndarray_creation(n, dtype=int):
    X = np.arange(n * n, dtype=dtype)
    X = X.reshape((n, n))
    return X

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=int):
    if type == 0:
        return np.zeros(shape, dtype=dtype)
    elif type == 1:
        return np.ones(shape, dtype=dtype)
    elif type == 99:
        return np.empty(shape, dtype=dtype)

def change_shape_of_ndarray(X, n_row):
    size = X.size
    if n_row == 1:
        return X.reshape(-1)
    
    n_col = size // n_row
    return X.reshape(n_row, n_col)

def concat_ndarray(X_1, X_2, axis):
    if X_1.ndim == 1:
        X_1 = X_1.reshape(1, -1)
    if X_2.ndim == 1:
        X_2 = X_2.reshape(1, -1)
    
    try:
        concatenated = np.concatenate((X_1, X_2), axis=axis)
    except ValueError:
        return False
    return concatenated

def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(dtype)
    
    if axis == 99:
        mean = X.mean()
        std = X.std()
        Z = (X - mean) / std
    else:
        mean = X.mean(axis=axis, keepdims=True) # keepdims -> 축을 유지한다
        std = X.std(axis=axis, keepdims=True)
        Z = (X - mean) / std
    return Z


def save_ndarray(X, filename="test.npy"):
    np.save(filename, X)
    pass


def boolean_index(X, condition):
    boolean_True = eval(f"X {condition}")
    indices = np.where(boolean_True)
    return indices


def find_nearest_value(X, target_value):
    index = np.argmin(np.abs(X - target_value)) # abs -> 절댓값!
    return X[index]

def get_n_largest_values(X, n):
    return np.sort(X)[-n:][::-1]
