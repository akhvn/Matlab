import numpy as np
from math import log, pi, sin
import matplotlib.pyplot as plt


plt.figure(figsize=(7,7))
plt.title(r"$f(x) = sin(x)$")
plt.ylabel("Ось $\delta_{N}$")
plt.xlabel(r"Ось N")

def monte_carlo(a,b,val_of_fun):
  I = (b-a)*sum(val_of_fun)/len(val_of_fun)
  return I

n = [x for x in range(1000,51000,5000)]
f = lambda x: np.sin(x)
a = 0
b = np.pi
deltas = []
deltas_av = []
I_exact = 2.0
for j in range(len(n)):
  for i in range(100):
    r_i = np.random.uniform(a,b,n[j])
    val_of_fun = f(r_i)
    I_N = monte_carlo(a,b,val_of_fun)
    delta = abs(I_N - I_exact)/I_exact
    deltas.append(delta)
  delta_av = sum(deltas)/100
  deltas_av.append(delta_av)
  
  deltas = []
print('delta=',delta)
#print('deltas_av', deltas_av)
for k in range(len(n)):
  n[k] = log(n[k])
  deltas_av[k] = log(deltas_av[k])

from numpy import polyfit, poly1d
coefficients = polyfit( n, deltas_av, 1 ) 
print("alpha=", float(coefficients[0]))
p = poly1d(coefficients)
plt.scatter(n, deltas_av)
plt.plot(n,p(n))
plt.show()
