import pysal
import numpy as np

input_file = pysal.open('usjoin.csv')
pci = np.array([input_file.by_col[str(y)] for y in range(1929, 2010)])
pci = pci.transpose()

weights = pysal.open("states48.gal").read()
maxp = pysal.Maxp(weights, pci, floor=5, floor_variable=np.ones((48, 1)), initial=99)

names = input_file.by_col('Name')
names = np.array(names)

for region in maxp.regions:
    ids = map(int, region)
    print(", ".join(names[ids]))
