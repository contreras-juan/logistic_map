import random as rd
import numpy as np
import matplotlib.pyplot as plt

l_min = 2
l_max = 4
l_step = 200

for i in range(0, l_step):
    r = l_min * i * (l_max - l_min) / (l_step - 1)
    x = 0.52
    for j in range(0, 100):
        x = r * x * (1 - x)
    py = []
    for j in range(0, 200):
        x = r * x * (1 - x)
        py = py + [x]

    plt.xlabel('Growth rate')
    plt.ylabel('Equilibrium long-run population')
    plt.title('Logistic map')
    plt.plot([r] * 200, py, 'k,')
    plt.pause(0.0001)

plt.ioff()
plt.show()
