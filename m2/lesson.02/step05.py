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
print(temp_values)
print(temp_values.ndim)
print(temp_values.shape)
print(temp_values.size)
print(temp_values.dtype)

# temp_days = temp_values.reshape(14, 3)
temp_days = temp_values.reshape(-1, 3)
print(temp_days)
print(temp_days.ndim)
print(temp_days.shape)
print(temp_days.size)
print(temp_days.dtype)

temp_weeks = temp_values.reshape(-1, 7, 3)
print(temp_weeks)
print(temp_weeks.ndim)
print(temp_weeks.shape)
print(temp_weeks.size)
print(temp_weeks.dtype)