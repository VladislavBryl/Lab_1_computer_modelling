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
p = sum(scipy.stats.expon.pdf(x)) / n

print('The significance level α=0.05 and the number of degrees of freedom 19')
if p > 0.95:
    print('With a confidence probability of 0.95 the random variable is distributed '
          'according to the exponential distribution law.')
else:
    print('With a confidence probability of 0.95 the random variable is not distributed '
          'according to the exponential distribution law.')

# building a histogram
h = (max(x) - min(x)) / 20
intervals = []
for i in range(21):
    intervals.append(min(x) + h * i)

# the number of hits of the generated numbers in the intervals
y = [0 for i in range(20)]
for i in range(len(x)):
    for j in range(len(y)):
        if intervals[j] <= x[i] <= intervals[j + 1]:
            y[j] += 1

plt.bar(intervals[0:20], y, width=h, label='Generated function')
plt.show()