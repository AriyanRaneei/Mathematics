import numpy as np
from numpy.linalg import matrix_power


a = np.array([[1,2],[3,4]])
print(a)

print(np.matmul(a,a)) # indoor time

print(np.power(a,4))

b = np.array([[2,4],[7,6]])
print(matrix_power(b,3))
print(np.arange(10))
print(np.arange(1,10,2))
print(np.linspace(0,1,11))
