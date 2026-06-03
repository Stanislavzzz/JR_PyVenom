import numpy as np

zeros_array = np.zeros(7)

print(zeros_array)
print(zeros_array.ndim)
print(zeros_array.shape)
print(zeros_array.size)
print(zeros_array.dtype)
print(zeros_array.itemsize)

zeros_array = np.zeros(7, dtype=np.int32)

print(zeros_array)
print(zeros_array.ndim)
print(zeros_array.shape)
print(zeros_array.size)
print(zeros_array.dtype)
print(zeros_array.itemsize)

zeros_array = np.zeros(7, dtype=np.int64)

print(zeros_array)
print(zeros_array.ndim)
print(zeros_array.shape)
print(zeros_array.size)
print(zeros_array.dtype)
print(zeros_array.itemsize)

ones_array = np.ones(5, dtype=np.int64)

print(ones_array)
print(ones_array.ndim)
print(ones_array.shape)
print(ones_array.size)
print(ones_array.dtype)

empty_array = np.empty(9)

print(empty_array)
print(empty_array.ndim)
print(empty_array.shape)
print(empty_array.size)
print(empty_array.dtype)