import numpy as numpy
# 2x2 matrix with 1's on main diagonal
obj1 = numpy.eye(2, dtype = float)
print("Matrix : \n", obj1)
# matrix with Row=2 Column=3 and diagonal=1
obj2 = numpy.eye(3, 3, k = -2)
print("\nMatrix : \n", obj2)