import matplotlib.pyplot as plt
import numpy as np
from random import*
f=lambda x:4*r*x*(1-x)
x0=random()
r=float(input('введите r:'))
x=[f(x0)]
n=[i+1 for i in range(60)]
for i in range(59):
    x.append(f(x[-1]))
ax = plt.subplots()
plt.plot(n,x)
plt.show()
