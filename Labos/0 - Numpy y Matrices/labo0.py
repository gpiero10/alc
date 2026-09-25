import numpy as np

#(1)
def esCuadrada(A):
  return (A.shape[0] == A.shape[1])

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(esCuadrada(matrix))

#(2)
def trianguSup(A):
  for x in range(A.shape[0]):
    for y in range(A.shape[1]):
      if x >= y:
        A[x][y] = 0

  return A

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
trianguSup(matrix)

#(3)
def trianguInf(A):
  for x in range(A.shape[0]):
    for y in range(A.shape[1]):
      if y >= x:
        A[x][y] = 0

  return A

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
trianguInf(matrix)

#(4)
def diagonalD(A):
  for x in range(A.shape[0]):
    for y in range(A.shape[1]):
      if not(y == x):
        A[x][y] = 0

  return A

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
diagonalD(matrix)

#(5)
def traza(A):
  acumulado = 0
  for x in range(A.shape[0]):
        acumulado += A[x][x]
  return acumulado

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
traza(matrix)

#(6)
def traspuesta(A):
  dimensiones = A.shape
  res = np.zeros(dimensiones, np.int64)
  for x in range(dimensiones[0]):
    for y in range(dimensiones[1]):
      res[y][x] = A[x][y]
  return res

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
traspuesta(matrix)

#(7)
def esSimetrica(A):
  dimensiones = A.shape
  res = True
  for x in range(dimensiones[0]):
    for y in range(dimensiones[1]):
      res &= (A[x][y] == A[y][x])
  return res


matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
assert(esSimetrica(matrix) == False)

matrix2 = np.array([[1,2,3],
                    [2,5,6],
                    [3,6,9]])
assert(esSimetrica(matrix2) == True)

#(8)
def calcularAx(A, X):
  # dim(A)=nxm, dim(X)=mx1, dim(A*X)=n*1
  n = A.shape[0]
  m = A.shape[1]
  vec = np.zeros(n, np.int64)
  for i in range(n):
    for j in range(m):
      vec[i] += A[i][j]*X[j]
  return vec

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([1,2,3])
   
calcularAx(matrix, vector)

#(9)
def intercambiarFilas(A, i, j):
  dim = A.shape #n*m
  temp = 0
  for x in range(dim[1]):
    temp = A[i][x]
    A[i][x] = A[j][x]
    A[j][x] = temp

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
intercambiarFilas(matrix, 0, 1)
matrix

#(10)
def sumar_fila_multiplo(A,i,j,s):
  dim = A.shape
  for x in range(dim[1]):
    A[i][x] += (A[j][x])*s

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
sumar_fila_multiplo(matrix, 0, 1, 2)
matrix

#(11)
def esDiagonalmenteDominante(A):
  dim = A.shape
  res = True
  for x in range(dim[0]):
    valorFila = 0
    pivote = 0
    for y in range(dim[1]):
      if x != y:
        valorFila += abs(A[x][y])
      else:
        pivote = abs(A[x][x])
    res &= (pivote > valorFila)
  
  return res

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
assert(esDiagonalmenteDominante(matrix) == False)

matrix = np.array([[6,2,3],[4,11,6],[7,8,-16]])
assert(esDiagonalmenteDominante(matrix) == True)

#(12)
def matrizCirculante(v):
  n = v.size
  m = np.zeros((n,n), np.int32)
  
  puntero = 0
  for x in range(0,n):
    for y in range(0,n):
      m[x][y] = v[(puntero+y) % n]
    puntero = (puntero - 1) % n
  return m

v = np.array([1,2,3])
print(matrizCirculante(v))

#(13)
def matrizVandermonde(v):
  n = v.size
  m = np.zeros((n,n), int)
  for x in range(n):
    for y in range(n):
      if y == 0:
        m[x][0] = 1
      elif y == 1:
        m[x][1] = v[x]
      else:
        m[x][y] = m[x][y-1]*v[x]
  return m
    
print(matrizVandermonde(np.array([1,2,3])))

#(14)
def numeroAureo(n):
  ant = 1
  antant = 0
  cur = 0
  for x in range(2, n+1):
    cur = ant + antant
    antant = ant
    ant = cur

  return ant/antant

print(numeroAureo(5))

#(15)
def matrizFibonacci(n):
  fibo = np.zeros(2*n+1, int)
  fibo[0] = 0
  fibo[1] = 1
  for x in range(2, 2*n+1):
    fibo[x] = fibo[x-1] + fibo[x-2]

  m = np.zeros((n,n), int)
  for x in range(0, n):  
    for y in range(0, n):
      m[x][y] = fibo[x+y]
  return m

print(matrizFibonacci(5))

#(16)
def matrizHilbert(n):
  m = np.zeros((n,n), float)
  for x in range(0, n):  
    for y in range(0, n):
      m[x][y] = 1/(x+y+1)
  return m
print(matrizHilbert(4))

#(17)
def valuarPolinomio(P, V):
  n = P.size
  res = 0
  for x in range(0,n):
    res += V**x * P[x]
  return res
print(valuarPolinomio(np.array([3, 0, 1]), 2))

def calcularEnRangoEquispaciado(S,E):
  return

#(18)
#def row_echelon_modified(M):
