import numpy as np


# print(np.__version__)

data_2d_list = [
    [10, 20, 30, 40, 50],
    [1, 2, 3, 4, 5],
    [7, 8, 9, 11, 55],
]

array_2d = np.array(data_2d_list)

print(data_2d_list)
print(type(data_2d_list))
print(array_2d)
print(type(array_2d))

print(array_2d.ndim)
print(array_2d.shape)
print(array_2d.size)
print(array_2d.dtype)