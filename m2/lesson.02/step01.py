import numpy as np


# print(np.__version__)

data_list = [10, 20, 30, 40, 50]

array_1d = np.array(data_list)

# print(data_list)
# print(type(data_list))
# print(array_1d)
# print(type(array_1d))

print(array_1d.ndim)
print(array_1d.shape)
print(array_1d.size)
print(array_1d.dtype)