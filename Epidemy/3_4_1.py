import numpy as np
import matplotlib.pyplot as plt
import time

p_c = np.array([0.00001, 0.000015, 0.000026, 0.00006, 0.00016, 0.0002, 0.00025, 0.0009])
N = np.array([100000, 70000, 50000, 20000, 10000, 7000, 5000, 1000])
ln_p_c = np.log(p_c)
ln_N = np.log(N)
plt.plot(ln_p_c, ln_N, markersize = 1, color='indigo')
plt.show()
