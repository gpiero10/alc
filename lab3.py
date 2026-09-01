import numpy as np
import matplotlib as plt
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

p = [1,2,5,10,100,200]


l = np.zeros((10,2))

for i in range(10):
    t = np.random.rand(2)
    l[i][0] = t[0]
    l[i][1] = t[1]

y = norma(l, p[0])
y2 = norma(l, p[4]) 
y3 = norma(l, p[5])
plt.plot(l,y)
plt.plot(l,y2)
plt.plot(l,y3)
plt.show()

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


x = [1,65,-67]
print(normaWithPInf(x, np.inf))

# 2. Normas matriciales inducidas
def calcularAX(A, x):
    n,m = A.shape()
    res = np.array(n)
    for i in range(n):
        for j in range(m):
            res[i] += A[i][j]*x[j]

    return res

def normaMatMC(A,q,p,Np):
    n,m = A.shape()
    res = norma(calcularAX(A, np.random.rand(m)), q)
    for i in range(1, Np):
        res = max(norma(calcularAX(A, np.random.rand(m)), q), res)

    return res



