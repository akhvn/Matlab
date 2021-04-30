import random
from scipy import integrate
from math import sin, pi

func = lambda x: sin(x)
J = integrate.quad(func, 0, pi)
print('integral result =', J[0])

N = 100
l = []

for i in range(N):
    r = random.random()   #случайная точка
    funct = lambda x: sin(r)
    J1 = integrate.quad(funct, 0, pi)
    Jn= float(J1[0])
    deln = abs(Jn - float(J[0]))/float(J[0])
    l.append(deln)
m = sum(l)
d = m/N
print ('delta = ', d)
