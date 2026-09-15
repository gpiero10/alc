import numpy as np

#Ejercicio 3
# Estas funciones asumen que las matrices pasadas por parametro son inversibles y no necesitan intercambio de filas

# Deja ceros debajo de la diagonal -> U
def trianguladorInferiorSistemaAx_b(A,b):
    n,m = A.shape
    for i in range(n):   #fila pivote
        for j in range(i+1, n): #fila operada
            if A[j][i] == 0: continue
            escalar = (-1*A[j][i])/A[i][i]
            for k in range(m):   #columna
                A[j][k] += A[i][k]*escalar                 
            b[j] += b[i]*escalar
    return A, b

# Deja ceros arriba de la diagonal -> L
def trianguladorSuperiorSistemaAx_b(A,b):
    n,m = A.shape
    for i in range(n-1, -1, -1):   #fila pivote
        for j in range(i-1, -1, -1): #fila operada
            if A[j][i] == 0: continue
            escalar = (-1*A[j][i])/A[i][i]
            for k in range(m):   #columna
                A[j][k] += A[i][k]*escalar                 
            b[j] += b[i]*escalar
    return A, b

# Tests

# Caso triangulador inferior
# M = np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
# r = np.array([1,-7,-5,1])
# print(trianguladorInferiorSistemaAx_b(M,r))

# Caso triangulador superior
# M = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])
# r = np.array([1,-7,0,4])
# print(trianguladorSuperiorSistemaAx_b(M,r))

def solucionadorSistemaLy_b(L,b):
    # L (nxm) * y (mx1) = b (nx1)
    n,m = L.shape
    y = np.zeros(n)
    L, b = trianguladorInferiorSistemaAx_b(L,b)
    for i in range(n):
        y[i] = b[i]/L[i][i]
    return y 

# M = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[-3,0,0,1]])
# r = np.array([1,-7,-5,1])
# print(solucionadorSistemaLy_b(M,r))

def solucionadorSistemaUx_y(U,y):
    # U (nxm) * x (mx1) = y (nx1)
    n,m = U.shape
    x = np.zeros(n)
    U, y = trianguladorSuperiorSistemaAx_b(U,y)
    for i in range(n):
        x[i] = y[i]/U[i][i]

    return x
    
# M = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])
# r = np.array([1,-7,0,4])
# print(solucionadorSistemaUx_y(M,r))

# Ejercicio 4
#(a)
def calcularLU(A):
    n,m = A.shape
    E = np.eye(n) #Matrices elementales app

    for i in range(n):   #fila pivote
        for j in range(i+1, n): #fila operada
            if A[j][i] == 0: continue

            escalar = (-1*A[j][i])/A[i][i]
            for k in range(m):   #columna
                A[j][k] += A[i][k]*escalar                 

            matElem = np.eye(n)
            matElem[j][i] = escalar
            E = matElem@E

    L = np.linalg.inv(E) # E^-1 = L

    return L, A

# M = np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
# print(calcularLU(M)) # Si funciona :)

#(b)
def resolvedorAx_b(A,b):
    L,U = calcularLU(A)
    y = solucionadorSistemaLy_b(L,b)
    x = solucionadorSistemaUx_y(U, y)

    return x

M = np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
b = np.array([1,-7,-5,1])
print(resolvedorAx_b(M,b))  # Si funciona :)
