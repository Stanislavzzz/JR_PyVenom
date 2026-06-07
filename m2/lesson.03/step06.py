import numpy as np


data = np.array([
    [12, 5, 7, 3],
    [10, 6, 8, 4],
    [15, 4, 6, 2],
    [11, 7, 9, 5],
    [14, 17, 6, 15],
])

print(data)
print(data.shape)
print(data.sum())
print(data.min())
print(data.max())
print(data.mean())
print()
print()

print(data)
print()
print(data.sum(axis=0))
print(data.min(axis=0))
print(data.max(axis=0))
print(data.mean(axis=0))

print()
print()

print(data)
print()
print(data.sum(axis=1))
print(data.min(axis=1))
print(data.max(axis=1))
print(data.mean(axis=1))