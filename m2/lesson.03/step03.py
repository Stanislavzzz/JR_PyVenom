import numpy as np


data = np.array([
    [12, 5, 7, 3],
    [10, 6, 8, 4],
    [15, 4, 6, 2],
    [11, 7, 9, 5],
])

print(data)
print()

# new_data = data[1:3, 0:2]
# print(new_data)
# print()
#
# new_data[0, 0] = 777
# print(new_data)
# print()
#
# print(data)

print('*' * 50)

new_data1 = data[1:3, 0:2].copy()
print(new_data1)
print()


new_data1[0, 0] = 555
print(new_data1)
print()

print(data)