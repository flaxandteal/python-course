import random

with open('rainfall-radar.csv', 'w') as f:
    for i in range(20):
        for j in range(20):
            f.write("%d %d %.1lf\n" % (i + 1, j + 1, 3 * ((i - 13) / 10) ** 2 + random.random() * 1.0))
