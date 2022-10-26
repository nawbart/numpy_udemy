import numpy as np
from numpy import linalg as LA


print('zad 61', '\n')

A1 = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B1 = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])

r1 = (A1 + B1) / 2


print(r1, '\n')


print('zad 62', '\n')

A2 = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B2 = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])

r2 = (A2 * B2)


print(r2, '\n')


print('zad 63', '\n')

A3 = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])

r3 = np.sqrt(A3)

print(r3, '\n')

print('zad 64', '\n')

A4 = np.linspace(0, np.pi / 2, 20)
B4 = np.full(shape=(20,), fill_value=1, dtype='float')


r4 = np.allclose(np.sin(A4) ** 2 + np.cos(A4) ** 2, B4)

print(r4, '\n')


print('zad 65', '\n')

A5 = np.array([[2, 3],
              [-4, 2],
              [5, 0]])
B5 = np.array([[4, 3, 2],
              [-1, 0, 2]])


r5 = np.dot(A5, B5)

print(r5, '\n')


print('zad 66', '\n')

A6 = np.array([[-2, 0, 4],
              [5, 2, -1],
              [-4, 2, 4]])


r6 = LA.det(A6) # wartości własne i prawe wektory własne

print(r6, '\n')


print('zad 67', '\n')

A7 = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])


eigenvalues, eigenvectors = LA.eig(A7) # wartości własne i prawe wektory własne

print(eigenvalues, '\n', eigenvectors, '\n')


print('zad 68', '\n')

A8 = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])

r8 = LA.inv(A8)

print(r8, '\n')

print('zad 69', '\n')

A9 = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])

r9 = np.trace(A9)

print(r9, '\n')

print('zad70', '\n')

A70 = np.array([[2, 0],
              [4, 2],
              [5, 3],
              [4, 2]])
B70 = np.array([[4, 0, 2, 1, 1, 0, 2, 9]])

B701 = np.reshape(B70, (2,4))


r70 = np.dot(A70, B701)

print(r70, '\n')





A = np.array([[2, 0],
              [4, 2],
              [5, 3],
              [4, 2]])
B = np.array([[4, 0, 2, 1, 1, 0, 2, 9]])



































































































































