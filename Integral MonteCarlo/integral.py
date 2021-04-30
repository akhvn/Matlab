from scipy import integrate
from math import sin, pi

func = lambda x: sin(x)
res = integrate.quad(func, 0, pi)
print(res[0])
