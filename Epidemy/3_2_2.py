import matplotlib.pyplot as plt
from random import random
import math

N = 1000
def gen(p, c):
    sick = [1]
    for i in range(1, c):
        today = sick[-1] 
        healthy = N - today
        sickness = 0
        for ch in range(healthy):
            Ph_s = 1 - (1 - p) ** today 
            r = random()
            if r < Ph_s:
                sickness += 1
        sick.append(sickness)
    return sick

def f(p, count, avg, graf=False):
    illness = [0 for i in range(count)]
    days = [i for i in range(count)]
    for i in range(avg):
        illness_i = gen(p, count)
        if graf:
            plt.plot(days, illness_i, linewidth=1, color=(random(), random(), random()))
        for j in range(count):
            illness[j] += illness_i[j]/avg
    return illness

def graf(p, count, avg, graf=False):
    days = [i for i in range(count)]
    illness = f(p, count, avg, graf)
    plt.title(r"Кривая устредненная по многим розыгрышам")
    plt.plot(days, illness, linewidth=3, c='r')
    plt.show()
graf(0.006, 10, 10, True)
graf(0.006, 10, 10)
