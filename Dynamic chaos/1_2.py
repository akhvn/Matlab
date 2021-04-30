import matplotlib.pyplot as plt
import numpy as np
f=lambda x:4*r*x*(1-x)
x01=0.5
x02=0.51
r=float(input('введите r:'))
x=[f(x01)]
x2=[f(x02)]
n=[i+1 for i in range(150)]
for i in range(149):
    x.append(f(x[-1]))
for i in range(149):
    x3 = f(x2[-1])
    #x3 = x3/10
    #x3 = x3*10
    #x3 = x3/16
    #x3 = x3*16
    #x3 = x3/20
    #x3 = x3*20
    x2.append(x3)
ax = plt.subplots()

plt.plot(n,x, color = 'blue')
plt.plot(n,x2, color = 'yellow')
plt.show()
