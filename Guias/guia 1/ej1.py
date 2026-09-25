import numpy as np

a = np.array([[1,1,-2,1],[3,-2,1,5],[1,-1,1,2]])
b = np.array([-2,3,2])
x = np.linalg.solve(a,b)
print(x)