import numpy as np


data = np.array([
    [12, 5, 7, 3],
    [10, 6, 8, 4],
    [15, 4, 6, 2],
    [11, 7, 9, 5],
    [14, 17, 6, 15],
])

print(data)

mask = data > 7
print(mask)
print(mask.dtype)
print(mask.shape)

print()
print()

filtered = data[mask]
print(filtered)
print(filtered.dtype)
print(filtered.shape)

pass_count = mask.sum()
print(pass_count)
print()
print()
print()

mask = (data >= 7) & (data < 14)
filtered = data[mask]
print(filtered)
print(filtered.dtype)
print(filtered.shape)

pass_count = mask.sum()
print(pass_count)