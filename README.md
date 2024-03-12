# MATLAB Functions in Python

This project aims to provide a Python module that replicates essential MATLAB functions for users who are familiar with MATLAB and transitioning to Python. The module, `matlab_functions.py`, includes functions commonly used in MATLAB for array manipulation, random number generation, reshaping, and basic statistical operations.

## Features

- **Zeros and Ones Functions:** Create arrays of zeros or ones with a specified shape.

- **Eye Function:** Generate an identity matrix of a given size.

- **Linspace Function:** Generate linearly spaced vectors.

- **Magic Function:** Create a magic square (a matrix in which the sums of the elements in each row, column, and both main diagonals are the same).

- **Rand and Randn Functions:** Generate arrays of random numbers from uniform and normal distributions, respectively.

- **Reshape Function:** Reshape an array into a specified shape.

- **Size Function:** Get the size of an array or the size along a specified dimension.

- **Sum, Mean, and Std Functions:** Perform basic statistical operations on arrays.

## Usage

```python
import matlab_functions as mat

# Example Usage
print(mat.zeros((2, 3)))
print(mat.ones((3, 2)))
print(mat.eye(4))
print(mat.linspace(0, 1, 5))
print(mat.magic(3))
# Add more examples based on your functions
```

## Contributing

Contributions are welcome! If you have additional MATLAB functions you'd like to replicate or improvements to existing ones, feel free to open an issue or submit a pull request.

