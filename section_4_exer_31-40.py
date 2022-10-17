import numpy as np

print('zad 31', '\n')
A1 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

print(np.sort(A1, kind='mergesort')) # sortowanie wierszy

print(np.sort(A1, axis=0, kind='mergesort'), '\n') # sortowaniekolumn

print('zad 32', '\n')

A2 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

print(A2[A2>8], '\n')

print('zad 33', '\n')

A3 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(np.where(A3 < 10, A3, 10), '\n')

print('zad 34', '\n')

A4 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(np.ravel(A4), '\n')

print('zad 35', '\n')

A5 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(np.zeros_like(A5), '\n')

print('zad 36', '\n')

A6 = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(np.full_like(A6, 9.99), '\n')

print('zad 37', '\n')

r7 = np.tri(5, dtype=float)
print(r7, '\n')


print('zad 38', '\n')

A8 = np.array([[[4, 5, 4, 2],
               [6, 3, 5, 1],
               [5, 2, 1, 2]],

              [[7, 2, 3, 1],
               [6, 2, 0, 9],
               [0, 1, 9, 1]]])
print(A8, '\n')

print('zad 39', '\n')

A9 = np.random.randint(0, 256, (200,300), dtype= np.uint8)

print(A9, '\n')

print('zad 40', '\n')

A40 = np.random.randint(0, 256, (200,300), dtype= np.uint8)
image_sorted = np.sort(A40)
print(image_sorted)


















































