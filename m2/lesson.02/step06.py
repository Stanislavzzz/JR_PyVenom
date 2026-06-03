import numpy as np

#
# data_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(data_list)
#
# reshape_array = data_list.reshape(-1, 3)
# print(reshape_array)
# print()


resize_array = np.array([1, 2, 3, 4, 5, 6, 7])
print(resize_array)

resize_array.resize(9)
print(resize_array)
print(type(resize_array))

resize_array.resize(5)
print(resize_array)
print(type(resize_array))