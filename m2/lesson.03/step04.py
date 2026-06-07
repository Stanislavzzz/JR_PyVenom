import numpy as np


data = np.array([10, 5, 20, 30, 50])
delta = np.array([1, 2, 3, 4, 5])

print(data)
print(delta)

result = (data + delta) * 100
print(result)
result = data - delta
print(result)