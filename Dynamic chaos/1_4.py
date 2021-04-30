import matplotlib.pyplot as plt
import random

n = 1000
R = []
step_1 = 0
for k in range(1, 1000):
    x0 = random.random()
    a = []
    a.append(x0)
    r = 0.001*k
    for i in range(1, n):
        a.append(4*r*a[i-1]*(1-a[i-1]))
    for i in range(950, n - 2**step_1, 2**step_1):
        if round(a[i], 2) != round(a[i + 2**step_1], 2):
            print(r)
            R.append(r)
            step_1 += 1
            plt.scatter(r, a[i], s=0.5, color='red')
            break
    plt.scatter([r] * 50, y=a[950:], s=0.5, color='blue')

r1 = 0.75
r2 = 0.863
r3 = 0.887
r4 = 0.892
delta1 = (r2 - r1)/(r3 - r2)
delta2 = (r3 - r2)/(r4 - r3)
delta = (delta1 + delta2)/2
print(delta)
print(delta1)
print(delta2)

plt.show()
