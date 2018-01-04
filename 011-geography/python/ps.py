import os
import pysal
import numpy as np

examples = os.path.join(os.path.dirname(pysal.__file__), 'examples', 'us_income')

input_file = pysal.open(os.path.join(examples, 'usjoin.csv'))
pci = np.array([input_file.by_col[str(y)] for y in range(1929, 2010)])
pci = pci.transpose()

weights = pysal.open(os.path.join(examples, "states48.gal")).read()
maxp = pysal.Maxp(weights, pci, floor=5, floor_variable=np.ones((48, 1)), initial=99)

names = input_file.by_col('Name')
names = np.array(names)

for region in maxp.regions:
    ids = list(map(int, region))
    print(", ".join(names[ids]))
