import numpy as np

m1 = np.array([[1,4,7],[2,5,8],[3,4,5]])
m2 = np.array([[1,4,5],[1,5,2],[5,6,7]])

addition = np.add(m1, m2)
print("Element-wise addition:\n", addition)

subtraction = np.subtract(m1, m2)
print("Element-wise subtraction:\n", subtraction)

result_dot = np.dot(m1,m2)
print("Matrix multiplication (dot product):\n",result_dot)

result_divide = np.divide(m1,m2)
print("Matrix multiplication (dot product):\n",result_divide)

result_mod = np.mod(m1,m2)
print("Module of m1 to m2 is :\n",result_mod)

result_mul = np.multiply(m1, m2)
print( "Element-wise multiplication:\n",result_mul)



