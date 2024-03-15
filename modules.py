# matlab_functions.py

import numpy as np

def zeros(shape):
    """Replicates MATLAB's zeros function."""
    return np.zeros(shape)

def ones(shape):
    """Replicates MATLAB's ones function."""
    return np.ones(shape)

def eye(n):
    """Replicates MATLAB's eye function."""
    return np.eye(n)

def linspace(start, stop, num=50):
    """Replicates MATLAB's linspace function."""
    return np.linspace(start, stop, num)

def magic(n):
    """Replicates MATLAB's magic function."""
    if n % 2 == 1:
        return np.array([[n**2 - j - i * n + 1 for j in range(n)] for i in range(n)])
    else:
        print("Input size must be odd for the magic square.")
        return None

# matlab_functions.py

import numpy as np

def rand(*args):
    """Replicates MATLAB's rand function."""
    return np.random.rand(*args)

def randn(*args):
    """Replicates MATLAB's randn function."""
    return np.random.randn(*args)

def reshape(arr, shape):
    """Replicates MATLAB's reshape function."""
    return np.reshape(arr, shape)

def size(arr, dim=None):
    """Replicates MATLAB's size function."""
    if dim is None:
        return arr.shape
    else:
        return arr.shape[dim-1] if 1 <= dim <= len(arr.shape) else 1

def sum(arr, axis=None):
    """Replicates MATLAB's sum function."""
    return np.sum(arr, axis=axis)

def mean(arr, axis=None):
    """Replicates MATLAB's mean function."""
    return np.mean(arr, axis=axis)

def std(arr, axis=None):
    """Replicates MATLAB's std function."""
    return np.std(arr, axis=axis)

# Add more functions as needed.
