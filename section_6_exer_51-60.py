import numpy as np


print('zad 51', '\n')

AA1 = np.array([[3, 4, 5],
              [8, 3, 1]])
B1 = np.array([[0, 5, 2],
              [4, 2, 1]])

r1 = np.concatenate((AA1, B1), axis=0)
print(r1, '\n')



print('zad 52', '\n')

data = np.array([[4.3, 4.2],
                 [3.1, 3.6]])
target = np.array([[0],
                   [1]])

r2 = np.concatenate((data, target), axis=1)
print(r2, '\n')

print('zad 53', '\n')

feature1 = np.array([1.6, 0.9, 2.2])
feature2 = np.array([0.4, 1.3, 3.2])
feature3 = np.array([1.4, 0.3, 1.2])

r3 = np.column_stack((feature1,feature2,feature3))

print(r3, '\n')

print('zad 54', '\n')

A4 = np.random.randint(low=0, high=7, size=(5, 8))
A4[:, :2] = 0
A4[:, -2:] = 1

A1 = A4[::, :2:]
A2 = A4[::, 2:6:]
A3 = A4[::, 6::]


print(A1, '\n')
print(A2, '\n')
print(A3, '\n')


print('zad 55', '\n')

np.random.seed(42)
A5 = np.random.randint(low=0, high=2, size=(10, 6))

r5 = np.count_nonzero(A5)
print(r5, '\n')

print('zad 56', '\n')

np.random.seed(42)

np.set_printoptions(precision=4)

A6 = np.random.randn(10, 4)

print(A6, '\n')



print('zad 57', '\n')

np.set_printoptions(precision=8, suppress=True)
A7 = np.array([1.2e-6, 1.7e-7])

print(A7, '\n')


print('zad 58', '\n')

np.random.seed(42)
A8 = np.random.randn(8, 4)
r8 = np.delete(A8, [2], axis=1)

print(r8, '\n')

print('zad 59', '\n')
from numpy import linalg as LA

v = np.array([3, 4, -2])
r9 = LA.norm(v)

print(r9, '\n')


print('zad 60', '\n')

np.random.seed(42)
np.set_printoptions(edgeitems=10)

A60 = np.random.randint(10, size=(100, 30))

print(A60, '\n')



























































