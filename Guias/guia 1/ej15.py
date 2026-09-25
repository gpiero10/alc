import numpy as np
# Matriz del ejercicio
A = np.array([[-1,2,1],[1,0,-1],[1,1,3]])

B = np.array([[1, 0,1],[1,1,0],[0,1,1]])


A_inv = np.linalg.inv(A)
print(A_inv@B)