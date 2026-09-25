import numpy as np

1 + 3
a = 7
b = a + 1

print("b = ", b)

# Vectores
v = np.array([1 , 2 , 3 , -1])
w = np.array([ 2 , 3 , 0 , 5])

print("v + w = " , v + w)
print("2 ∗ v = " , 2*v )
print("v ∗∗ 2 = " , v**2 )

# M a t r i c e s ( e j e c u t a r l o s comandos uno a uno para v e r l o s r e s u l t a d o s )
A = np.array( [ [ 1 , 2 , 3 , 4 , 5 ] , [ 0 , 1 , 2 , 3 , 4 ] , [ 2 , 3 , 4 , 5 , 6 ] , [ 0 , 0 , 1 , 2 , 3 ] , [ 0 , 0 , 0 , 0 , 1 ] ] )
print(A)

print(A[0:2, 3:5])
print(A[:2, 3:])

print(A[[0, 2, 4], :])
ind = np.array([0, 2, 4 ])
print(A[ind,ind])
print(A[ind, ind [:, None]])

# Numeros c o m p l e j o s
print(1j * 1j)
print((1+2j) *1j)