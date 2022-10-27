import numpy as np
from numpy import linalg as LA


print('zad 71', '\n')

np.random.seed(42)

A1 = np.array([['id', 'price'],
              ['001', 14.99],
              ['002', 4.99],
              ['003', 7.99],
              ['004', 2.49],
              ['005', 1.49]])

np.random.shuffle(A1[1::])


print(A1, '\n')


print('zad 72', '\n')


A2 = np.array([0.2, 0.15, 0.1, 0.3, 0.2, 0.05])

r2 = np.argsort(A2)


print(r2, '\n')

print('zad 73', '\n')

np.random.seed(42)
A3 = np.random.randn(10, 8)

r3 = np.round(A3, decimals=3)


print(r3, '\n')

print('zad 74', '\n')

A4 = np.array([4, 5, 1])
r4 = np.roots(A4)

print(r4, '\n')

print('zad 75', '\n')

A5 = np.array([2, 4, -5, 1])
B5 = np.array([4, 0, -5, 1])

ra5 = np.roots(A5)
rb5 = np.roots(B5)

print(ra5, '\n')
print(rb5, '\n')

print('zad 76', '\n')
'''
A6 = np.array([0, 4, 5, 1])
B6 = np.array([2, 4, -5, 1])


sum = A6 + B6
subtraction = A6 - B6
multiply = A6 * B6
sum_multiply  = A6 + 2*(B6)

print(sum, '\n')
print(subtraction, '\n')
print(multiply, '\n')
print(sum_multiply, '\n')
'''

W6 = np.array([4, 5, 1])
Q6 = np.array([2, 4, -5, 1])

print(np.polyadd(W6, Q6))
print(np.polysub(W6, Q6))
print(np.polymul(W6, Q6))
print(np.polyadd(W6, 2 * Q6))

print('zad 77', '\n')

A7 = np.array([[-4, 3, 0, 1, -5],
              [6, -4, -2, 1, 3]])

r7 = np.sign(A7)
print(r7, '\n')


print('zad 78', '\n')

r8 = np.arange('2021-01-01', '2021-02-01', dtype='datetime64[D]')
print(r8, '\n')


print('zad 79', '\n')

r9 = np.arange('2021-01', '2022-01', dtype='datetime64[M]')
r9 = r9.reshape((4,3))

print(r9, '\n')


print('zad 80', '\n')

r80 = np.datetime64('today')

print(r80, '\n')

















































































































































