import numpy as np
import matplotlib.pyplot as plt #libreria para graficar

# ...
# Aca, crear matriz y resolver para a, b y c.

m = np.array([[1,1,1], [4,2,1], [9,3,1]])
s = np.array([1,2,0])
x = np.linalg.solve(m,s)
print(x)
# ...

a = -1.5
b = 5.5
c = -3

xx = np.array([1, 2 , 3])
yy = np.array([ 1 , 2 , 0 ])
x = np.linspace(0, 4, 100) #g e n e r a 100 puntos e q u i e s p a c i a d o s e n t r e 0 y 4 .
f = lambda t : a*t**2 + b*t +c #e s t o g e n e r a una f u n c i o n f de t .
plt.plot(xx , yy, '*')
plt.plot(x , f(x))
plt.show()

