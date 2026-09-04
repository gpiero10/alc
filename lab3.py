import numpy as np
import matplotlib.pyplot as plt

## 1. NORMAS
def norma(x,p):
    x = np.array(x)
    ac = 0
    for i in range(x.size):
        ac += x[i]**p
    return ac**(1/p)

def normaliza(X,p):
    n = len(X)
    m = len(X[0])
    y = np.zeros((n, m))
    for i in range(n):
        y[i] = X[i]/norma(X[i], p)
    return y

# ||(x,y)||_p = 1 -> x^p + y^p = 1^p -> y = +- (1 - x^p)^1/p 
# p = [1,2,5,10,100,200]
# x = np.linspace(-1, 1, 1000)
# for i in range(len(p)):
#     y = (1 - abs(x)**(p[i]))**(1/p[i])
#     plt.plot(x,y)
#     plt.plot(x,-y)
# plt.show()

def normaWithPInf(x,p):
    if np.isposinf(p) == True:
        r = abs(x[0])
        for i in range(1,len(x)):
            r = max(r, abs(x[i]))
        return r
    else:
        x = np.array(x)
        ac = 0
        for i in range(x.size):
            ac += x[i]**p
        return ac**(1/p)

# 2. Normas matriciales inducidas
def calcularAX(A, x):
    n,m = A.shape
    res = np.zeros(n)
    for i in range(n):
        for j in range(m):
            res[i] += A[i][j]*x[j]
    return res

def normaMatMC(A,q,p,Np):
    n,m = A.shape
    res = -1
    vector = np.zeros(m)
    for i in range(Np):
        v = np.random.rand(m)
        vNormalizado = v/norma(v, p)
        normaQdeAx = normaWithPInf(calcularAX(A,vNormalizado), q)
        if normaQdeAx > res:
            res = normaQdeAx
            vector = v

    return [res, vector]

print(normaMatMC(np.eye(2), 2, 1,1000))
print(normaMatMC(np.eye(2), 1, 2,1000))
print(normaMatMC(np.eye(2), 2, np.inf,1000))
print(normaMatMC(np.eye(2), np.inf, 2,1000))
print(normaMatMC(np.array([[0,-1],[1,0]]), 2, 2,1000))
print(normaMatMC(np.array([[1,0],[0,0]]), 2, 2,1000))
print(normaMatMC(np.array([[1,0],[0,0]]), np.inf, np.inf,1000))
print(normaMatMC(np.array([[10,10],[0,0]]), 2, np.inf,1000))

def normaExacta(A, p):
    # p = [1, inf]
    n, m = A.shape
    res = -1
    if np.isposinf(p) == True:
        for i in range(n):
            filaIesimaSum = 0
            for j in range(m):
                filaIesimaSum += abs(A[i][j])
            res = max(res, filaIesimaSum)
    if p == 1:
        for i in range(m):
            columnaIesimaSum = 0
            for j in range(n):
                columnaIesimaSum += abs(A[j][i])
            res = max(res, columnaIesimaSum)
    return res

# 3. Condicionamiento de Matrices
def condMC(A,p):
    # condA = ||A||p ||A^-1||p
    c1 = normaMatMC(A, p, p, 1000)
    invA = np.linalg.inv(A) 
    c2 = normaMatMC(invA, p, p, 1000)
    return c1*c2

def variaPerc(b, perc):
    n = len(b)
    k = np.ramdom.uniform(1-perc/100,1+perc/100)
    for i in range(n):
        b[i] *= k
    return b

def errorRelativoNormaP(x,xMonio, p):
    return normaWithPInf(x-xMonio,p)/normaWithPInf(x, p)

def buscarPeorVariacion(A, p, perc, NP):
    # A inversible -> A@x=b -> x = A^-1 @ b
    n,m = A.shape
    invA = np.linalg.inv(A)
    erroresX = []
    erroresB = []

    maximoErrorX = -1
    bMax = np.zeros(n)
    bMonioMax = np.zeros(n)

    for i in range(NP):
        b = np.random.rand(n)
        bMonio = variaPerc(b)
        x = invA @ b
        xMonio = invA @ bMonio
        errorX = errorRelativoNormaP(x, xMonio, p)

        if errorX > maximoErrorX:
            maximoErrorX = errorX
            bMax = b
            bMonioMax = bMonio

        erroresX.append(errorX)
        erroresB.append(errorRelativoNormaP(b, bMonio, p))
        
    condA = condMC(A,p)

    return erroresB, erroresX, condA, maximoErrorX, bMax, bMonioMax
