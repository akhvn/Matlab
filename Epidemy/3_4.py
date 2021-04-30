import matplotlib.pyplot as plt
from random import random
import math
from tqdm import tqdm

def generate(p, count):
    N=1000
    ill = [1]
    for i in range(1, count):
        # число заболевших сегодня
        n = ill[-1]
        # число здоровых
        z = N - n
        
        illness = 0
        for person in range(z):
            # вероятность что здоровый человек заболеет
            P = 1 - (1 - p) ** n
            r = random()
            if r < P:
                illness += 1
        ill.append(illness)
    return ill
#print(generate(0.006,10))

def generate_avg(p, count, avg, draw_avg=False):
    illness = [0 for i in range(count)]
    days = [i for i in range(count)]
    for i in range(avg):
        illness_i = generate(p, count)
        if draw_avg:
            plt.plot(days, illness_i, linewidth=1, color=(random(), random(), random()))
        for j in range(count):
            illness[j] += illness_i[j]/avg
    return illness
#print(generate_avg(0.06,10,3))

def draw_pc(prob, count, avg):
    Pr = [i/prob/10000*3 for i in range(prob)]
    Ill = []
    for i in range(prob):
        p = Pr[i]
        n1, n2 = generate_avg(p, count, avg)[-2:]
        Ill.append(n1 /2 + n2 / 2)
    #plt.plot(Pr, Ill, color='pink')
    #plt.show()
    #print(Ill)
    return Pr, Ill

N_list = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
res = []
for N in N_list:
    Pr0, Ill0 = draw_pc(100, 50, 3)
    print('N = ', N)
    for x in range(len(Ill0)):
        if Ill0[x] != 0:
            res.append(Pr0[x - 1])
            print(Pr0[x - 1])
            break
#print(res)
#plt.plot(N_list,res)
#plt.show()

