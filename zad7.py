import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

print(np.equal(A, B))
'''
z = zip(A, B)
l = []

for i, j in z:
    if i == j:
        l.append(True)
    else:
        l.append(False)

print(l)


'''