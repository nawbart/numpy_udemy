import numpy as np


#zad 21
a21 = np.ndarray(shape=(3, 4), dtype=int, buffer=np.arange(0, 12))

np.save('array21', a21)
res21 = np.load('array21.npy')
print(res21)



#zad 22
a22 = np.arange(12, dtype='int').reshape(-1, 4)

np.savetxt('array.txt', a22)
res22 = np.loadtxt('array.txt')
print(res22)


#zad 23


a23 = np.arange(12, dtype='int').reshape(3, 4)

r23 = a23.tolist()

print(r23)


#zad 24

a24 = np.arange(12, dtype='int').reshape(3, 4)
r24 = a24[::-1]
print(r24)


#zad 25

a25 = np.ones((4,4), dtype=int)
r25 = np.pad(a25, (1, 0), constant_values=0)  #(1,0) to rozmiar marginesu
print(r25)


#zad 26

a26 = np.zeros((6, 6), dtype='int')
a26[::2, ::2] = 10
a26[1::2, ::2] = 5

print(a26)

#zad 27

a27 = np.arange(12).reshape(-1, 4)
b27 = np.array([[4, 3, 7, 2],
               [0, 5, 2, 6]])

print(a27)
print("---------------")
print(b27)
print("---------------")
r27 = np.append(a27, b27, axis=0)  #axis pozwoliło na nadanie kolejnego wymiaru
print(r27)


#zad 28


a28 = np.arange(8).reshape(-1, 4)
b28 = np.array([[9, 10, 11, 3],
               [2, 8, 0, 9]])

r28 = np.intersect1d(a28, b28)
print(r28)

#zad 29

a29 = np.array([[5, 1, 2, 1, 2],
               [9, 1, 9, 7, 5],
               [4, 1, 5, 7, 9]])

r29 = np.unique(a29)
print(29)

#zad 30

a30 = np.array([[0.4, 0.3, 0.3],
               [0.1, 0.1, 0.8],
               [0.2, 0.5, 0.3]])

r30 = np.argmax(a30, axis=0)
print(r30)































































