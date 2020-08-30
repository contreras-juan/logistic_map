import random as rd
import numpy as np
import matplotlib.pyplot as plt


def logistic_diff_eq(r, x0, n):
    x = x0
    serie = []
    for i in range(1, n):
        x = r * x * (1 - x)
        serie.append(x)

    return f'The long-run equilibrium is {1 - 1 / r}'
