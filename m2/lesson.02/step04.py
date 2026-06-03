import numpy as np


time_sec = np.arange(5, 60, 10)
print(time_sec)
print(time_sec.ndim)
print(time_sec.shape)
print(time_sec.nbytes)
print(time_sec.size)
print(time_sec.dtype)

param_sec = np.linspace(5, 60, 10)
print(param_sec)
print(param_sec.ndim)
print(param_sec.shape)
print(param_sec.size)
print(param_sec.dtype)