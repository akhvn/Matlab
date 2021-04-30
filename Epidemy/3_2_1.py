import matplotlib.pyplot as plt
from random import random
import math

N = 1000
def f(p, c):
    sick = [1]
    for i in range(1, c):
        n = sick[-1] #сегодня
        healthy = N - n
        sickness = 0
        for ch in range(healthy):
            Ph_s = 1 - (1 - p) ** n #вероятность что здоровый заболеет
            r = random()
            if r < Ph_s:
                sickness += 1
        sick.append(sickness)
    return sick

def graf(p, c):
    days = [x for x in range(c)]
    illness = f(p, c)
    plt.title(r"Зависимости числа больных по дням эпидемии для разных значений p")
    plt.plot(days, illness, linewidth=1, color ='purple')
    plt.show()
print(f(0.006,10))
graf(0.6,100)
