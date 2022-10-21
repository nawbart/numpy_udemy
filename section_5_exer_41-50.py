import numpy as np

print('zad 41', '\n')
A1 = np.array([[4, 2, 1],
              [6, 4, 2]])


print(np.expand_dims(A1, axis=0), '\n')

print('zad 42', '\n')

np.random.seed(42)

A2 = np.random.randint(0, 256, (200,300,3), dtype= np.uint8)
print(A2, '\n')

print('zad 43', '\n')

A3 = np.random.randint(
low=0, high=256, size=(200, 300, 3), dtype=np.uint8)

print(np.expand_dims(A3, axis=0), '\n')

print('zad 44', '\n')

image1 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)
image2 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)

a4 = np.expand_dims(image1, axis=0)
b4 = np.expand_dims(image2, axis=0)
images = np.append(a4, b4, axis=0)
print(images, '\n')



print('zad 45', '\n')

A5 = np.array([[[1, 2, 3],
               [6, 3, 2]]])
print(np.shape(A5)) #shape(1,2,3)
r5 = np.squeeze(A5, axis=0) #shape(2,3)
print(r5.shape, '\n')

print('zad 46', '\n')

A6 = np.array([[0.4],
              [0.9],
              [0.5],
              [0.6]])

print(A6.shape)

r6 = np.squeeze(A6)
print(r6, '\n')

print('zad 47', '\n')

A7 = np.arange(12, dtype='int').reshape(3,4)

print(A7)

r7 = A7[::, ::-1]
print(r7, '\n')

print('zad 48', '\n')

A8 = np.arange(12, dtype='int').reshape(3,4)

r8 = A8[::-1, ::-1]

print(r8, '\n')


print('zad 49', '\n')

np.random.seed(42)

image9 = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8)

print(image9)
print(image9[:, :, 0], '\n')


print('zad 50', '\n')

image0 = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8)

print(image9[5:, 5:, :], '\n')








































