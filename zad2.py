import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

t = list('ABC')
a = (A, B, C)
r = zip(t, a)

for idx, a in r:
    print(f'{idx}: {np.all(a, axis=1)}')