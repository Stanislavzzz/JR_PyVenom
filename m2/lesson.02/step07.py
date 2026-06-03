import numpy as np


data_temp = [
    18.2, 18.9, 19.4,
    18.0, 18.7, 19.1,
    17.8, 18.6, 19.0,
    18.1, 18.8, 19.3,
    18.4, 19.0, 19.6,
    18.6, 19.2, 19.8,
    18.3, 19.1, 19.7,
    18.0, 18.8, 19.2,
    17.9, 18.5, 18.9,
    18.2, 18.9, 19.4,
    18.5, 19.1, 19.7,
    18.7, 19.4, 20.0,
    18.4, 19.0, 19.5,
    18.1, 18.7, 19.1
]

temp_values = np.array(data_temp)
print(temp_values.ndim)
print(temp_values[1])
print(temp_values[-1])
print(temp_values[2:6])
print(temp_values[::3])


temp_days = temp_values.reshape(-1, 3)
print(temp_days)
print(temp_days.ndim)
print(temp_days[1][2])
print(temp_days[1, 2])
row_arr = temp_days[2]
print(row_arr)
print(row_arr.shape)
print(type(row_arr))

print('*' * 50)
row_arr2 = temp_days[2:7, 1:]
print(row_arr2)