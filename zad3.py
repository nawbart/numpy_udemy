import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

l = list('ABCD')
a = [A, B, C, D]
r = zip(l, a)

for idx, a in r:
    print(f'{idx}: {np.any(a,)}')