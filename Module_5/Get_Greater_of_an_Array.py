from random import random

x = 20
y = []
avg = 0

for i in range(x):
    y.append(random())
    print("%5.2f" % y[i], end=' ')
    avg += y[i]
print()

average = avg/x
print("The average of the array = %.2f" % average)
for i in y:
    if i > average:
        print("%4.2f" % i)