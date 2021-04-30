import matplotlib.pyplot as plt
import numpy as np
from random import*
f=lambda x:4*r*x*(1-x)
def X(n):
    st=[f(x0)]
    while len(st)<n:
        st.append(f(st[-1]))
    return st[-1]
x=[]
z_r=[z/100000 for z in range(1,100001)]
for r in z_r:
    x0=random()
    x.append(X(2000))
ax = plt.subplots()
plt.scatter(z_r,x,0.1)
plt.show()
