import random

for i in range(21):
  for j in range(21):
    print(i, j, "%.1lf" % (0.025 * (200 - (i - 10) ** 2 - (j - 10) ** 2) + random.uniform(-0.5, 0.5)))
