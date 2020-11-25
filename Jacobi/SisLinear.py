import numpy as np

A = np.array([[1,3,1],[5,2,2],[0,6,8]])
B = np.array([[-2],[3],[-6]])
y = np.linalg.solve(A,B)
print(y)



