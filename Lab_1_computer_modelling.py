import matplotlib.pyplot as plt
from random import random
import math
import scipy.stats

n = 10000
gamma = 4510129875
print('gamma = ', gamma)
x = []
for i in range(n):
    ksi = random()
    x.append(- math.log(ksi) / gamma)

# checking for compliance with the exponential law of distribution
exp = scipy.stats.expon.rvs(scale=0.25 * 10 ** (-9), size=10000)
p = scipy.stats.chisquare(f_obs=sorted(x), f_exp=sorted(exp), ddof=19)[1]

print('The significance level α=0.05 and the number of degrees of freedom 19')
if p > 0.95:
    print('With a confidence probability of 0.95 the random variable is distributed '
          'according to the exponential distribution law.')
else:
    print('With a confidence probability of 0.95 the random variable is not distributed according to the exponential '
          'distribution law.')

    # Graphs
    plt.plot(sorted(x, reverse=True), label='Graph of the generated function')
    plt.plot(sorted(exp, reverse=True), label='Graph of the exponential function')
    plt.legend()
    plt.show()
    # building a histogram
    h = (max(x) - min(x)) / 20
    intervals = []
    for i in range(21):
        intervals.append(min(x) + h * i)

    # the number of hits of the generated numbers in the intervals
    y = [0 for i in range(20)]
    y_exp = [0 for i in range(20)]
    for i in range(len(x)):
        for j in range(len(y)):
            if intervals[j] <= x[i] <= intervals[j + 1]:
                y[j] += 1
            if intervals[j] <= exp[i] <= intervals[j + 1]:
                y_exp[j] += 1

    plt.subplot(2, 1, 1)
    plt.bar(intervals[0:20], y, width=h, label='Generated function')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.bar(intervals[0:20], y_exp, width=h, label='Exponential function')
    plt.legend()
    plt.show()
