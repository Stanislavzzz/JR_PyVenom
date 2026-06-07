import numpy as np


data = np.array([
    [12, 5, 7, 3],
    [10, 6, 8, 4],
    [15, 4, 6, 2],
    [11, 7, 9, 5],
])

print(data)
print()

data[1, 2] = 99
# data[1][2] = 99
print(data)