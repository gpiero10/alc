import numpy as np











#Modulo
def rota(theta):
    # Recibe un angulo theta y retorna una matriz de 2x2 que rota un vector dado en un angulo theta
    m = np.zeros((2,2), dtype=np.float64)
    m[0][0] = np.cos(theta)
    m[0][1] = -np.sin(theta)
    m[1][0] = np.sin(theta)
    m[1][1] = np.cos(theta)

    return m

def escala(s) :
    # Recibe una tira de numeros s y retorna una matriz cuadrada de
    # nxn, donde n es el tamano de s .
    # La matriz escala la componente i de un vector de Rn en un factor s[i]
    n = len(s)
    m = np.zeros((n,n), dtype=np.float64)
    for i in range(n):
        m[i][i] = s[i]

    return m

def multiplicacionDeMatrices(A,B):
    # retorna A @ B 
    n,m = A.shape
    x,y = B.shape

    r = np.zeros((n,y), dtype=np.float64)

    for i in range(n):
        for j in range(y):
            for e in range(x):
                r[i][j] += A[i][e] * B[e][j]

    return r

def rota_y_escala(theta, s):
    # R e c i b e un a n g u l o t h e t a y una t i r a de numeros s ,
    # y r e t o r n a una m a t r i z de 2 x2 que r o t a e l v e c t o r en un a n g u l o t h e t a y l u e g o l o
    # e s c a l a en un f a c t o r s
    A = escala(s)
    B = rota(theta)

    return multiplicacionDeMatrices(A,B)

def afin(theta, s, b):

    # R e c i b e un a n g u l o t h e t a , una t i r a de numeros s ( en R2) , y un v e c t o r b en R2 .
    # Retorna una m a t r i z de 3 x3 que r o t a
    # e l v e c t o r en un a n g u l o t h e t a , l u e g o l o e s c a l a en un f a c t o r s y por u l t i m o l o mueve en un v a l o r fijo b
    
    m = multiplicacionDeMatrices(escala(s), rota(theta))
    C = np.eye(3)
    C[0][0] = m[0][0]
    C[0][1] = m[0][1]
    C[1][0] = m[1][0]
    C[1][1] = m[1][1]

    C[0][2] = b[0]
    C[1][2] = b[1]

    return C


def trans_afin(v, theta, s, b):

    # R e c i b e un v e c t o r v ( en R2 ) , un a n g u l o t h e t a ,
    # una t i r a de numeros s ( en R2) , y un v e c t o r b en R2 .
    # Retorna e l
    # v e c t o r w r e s u l t a n t e de a p l i c a r l a t r a n s f o r m a c i o n a f i n a v
    
    R = multiplicacionDeMatrices(rota_y_escala(theta, s), np.array(v).reshape(2,1))

    R[0] += b[0] 
    R[1] += b[1]

    return R.reshape(2)

# Tests para rota
assert (np.allclose(rota(0), np.eye(2)))
assert (np.allclose(rota(np.pi / 2), np.array([[0, -1], [1, 0]])))
assert (np.allclose(rota(np.pi), np.array([[-1, 0], [0, -1]])))

# Tests para escala
assert (np.allclose(escala([2, 3]), np.array([[2, 0], [0, 3]])))
assert (np.allclose(escala([1, 1, 1]), np.eye(3)))
assert (np.allclose(escala([0.5, 0.25]), np.array([[0.5, 0], [0, 0.25]])))

# Tests para rota y escala
assert (
    np.allclose(
        rota_y_escala(0, [2, 3]),
        np.array([[2, 0], [0, 3]])
    )
)

assert (
    np.allclose(
        rota_y_escala(np.pi / 2, [1, 1]),
        np.array([[0, -1], [1, 0]])
    )
)

assert (
    np.allclose(
        rota_y_escala(np.pi, [2, 2]),
        np.array([[-2, 0], [0, -2]])
    )
)

# Tests para afin
assert (
    np.allclose(
        afin(0, [1, 1], [1, 2]),
        np.array([[1, 0, 1],
                   [0, 1, 2],
                   [0, 0, 1]])
    )
)

assert (
    np.allclose(
        afin(np.pi / 2, [1, 1], [0, 0]),
        np.array([[0, -1, 0],
                   [1, 0, 0],
                   [0, 0, 1]])
    )
)

assert (
    np.allclose(
        afin(0, [2, 3], [1, 1]),
        np.array([[2, 0, 1],
                   [0, 3, 1],
                   [0, 0, 1]])
    )
)

# Tests para transafin
assert (
    np.allclose(
        trans_afin(np.array([1, 0]), np.pi/2, [1, 1], [0, 0]),
        np.array([0, 1])
    )
)

assert (
    np.allclose(
        trans_afin(np.array([1, 1]), 0, [2, 3], [0, 0]),
        np.array([2, 3])
    )
)

assert (
    np.allclose(
        trans_afin(np.array([1, 0]), np.pi / 2, [3, 2], [4, 5]),
        np.array([4, 7])
    )
)

print("Logrado")