#!/usr/bin/python3

"""
Estimate the integral of sin(x) from 0, to pi.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def check_integral(numTrials):
    count = 0
    for i in range(numTrials):
        x = random.uniform(0, np.pi)
        y = random.random()
        if y <= np.sin(x):
            count += 1
    # print((count/numTrials)*np.pi)
    return (count/numTrials)*np.pi
# check_integral(1000)

def monte_carlo(num_samples, numTrials):
    means = []
    for i in range(num_samples):
        means.append(check_integral(numTrials))
    sample_mean = sum(means)/len(means)
    print('Sample mean is:', sample_mean)
    plt.hist(means)
    plt.show()

monte_carlo(20000, 10)