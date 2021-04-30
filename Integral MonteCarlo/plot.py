import numpy as np
import math
from math import log, sin, pi, cos
import matplotlib.pyplot as plt


plt.figure(figsize=(7,7))
plt.title(r"$f(x) = x^2$")
plt.ylabel("Это ось $\delta_{N}$")
plt.xlabel(r"Это ось N")

def monte_carlo(a,b,val_of_fun):
  I = (b-a)*sum(val_of_fun)/len(val_of_fun)
  return I

n = [x for x in range(1000,11000,1000)]
f = lambda x: math.sin(x)
a = 0
b = math.pi
deltas = []
deltas_av = []
I_exact = 2.66
for j in range(10):
  for i in range(100):
    r_i = np.random.uniform(a,b,n[j])
    val_of_fun = f(r_i)
    I_N = monte_carlo(a,b,val_of_fun)
    delta = abs(I_N - I_exact)/I_exact
    
    deltas.append(delta)
  delta_av = sum(deltas)/100
  deltas_av.append(delta_av)
  deltas = []
for k in range(10):
  n[k] = log(n[k])
  deltas_av[k] = log(deltas_av[k])
# from scipy.interpolate import interp1d
from numpy import polyfit, poly1d
coefficients = polyfit( n, deltas_av, 1 ) #where 1 is the degree of freedom
p = poly1d(coefficients)
plt.scatter(n, deltas_av)
plt.plot(n,p(n))
