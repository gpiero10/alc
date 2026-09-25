import numpy as np
import matplotlib.pyplot as plt


#Ej 2
a = 1.0
while a > 0.1:
    print(a)
    a = a - 0.1
print('fin')

#Ej 3

#Ej 4
print((np.sqrt(2))**2 - 2)

x = np.linspace(0.5, 1e-8, 100)
def a(x):
    return np.sqrt(2*(x**2)+1)-1
y = a(x)

plt.plot(x, y)

def b(x):
    return (2*x**2)/(np.sqrt(2*x**2+1)+1)
y2 = b(x)
plt.plot(x, y2)
plt.show()


#EJ 5
l = []
def raices():
    r = np.sqrt(2)
    l.append(r)
    for i in range(1,100):
        l.append(l[i-1]**2/np.sqrt(2))
    return l

b = raices()
plt.plot(b)
plt.show()

#Ej 6




#Modulo
def esSimetrica(A):
    x, y = A.shape
    for i in range(x):
        for j in range(y):
            if A[i][j] != A[j][i]: return False
    return True


def error(x,y):
    # Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
    x = np.float64(x)
    y = np.float64(y)
    return abs(x-y)

def error_relativo(x,y):
    #Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64
    x = np.float64(x)
    y = np.float64(y)

    if x == 0: return y
    if y == 0: return x

    return abs(x-y)/abs(x)
        

def matricesIguales(A,B):
    #Devuelve True si ambas matrices son iguales y False en otro caso.
    #Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.

    dimA = A.shape
    dimB = B.shape
    if dimA != dimB: return False

    eps = 1e-9

    for x in range(dimA[0]):
        for y in range(dimA[1]):
            if error(A[x][y], B[x][y]) > eps : return False

    return True



def sonIguales( x ,y, atol=1e-8):
    return np.allclose(error(x,y),0,atol=atol)

assert(not sonIguales(1,1.1))
assert(sonIguales(1,1 + np.finfo('float64').eps))
assert(not sonIguales(1,1 + np.finfo('float32').eps))
assert(not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps))
assert(sonIguales(np.float16(1),np.float16(1) + np.finfo('float16').eps,atol=1e-3))

assert(np.allclose(error_relativo(1,1.1),0.1))
assert(np.allclose(error_relativo(2,1),0.5))
assert(np.allclose(error_relativo(-1,-1),0))
assert(np.allclose(error_relativo(1,-1),2))

assert(matricesIguales(np.diag([1,1]),np.eye(2)))
assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2)))
assert(not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]])))
print("Tests pasados!")