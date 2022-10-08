import numpy as np


#zad 21
a21 = np.ndarray(shape=(3,4), dtype=int, buffer=np.arange(0,12))
print(a21)


np.save('array21', a21)



# numpy.save(file, arr, allow_pickle=True, fix_imports=True)
'''
#zad 22
from tempfile import TemporaryFile

s = TemporaryFile()



#zad 23


A = np.arange(12, dtype='int').reshape(3,4)

r = A.tolist()

print(r)


#zad 24

a = np.arange(12, dtype='int').reshape(3,4)
r = a[::-1]
print(r)


#zad 25

a = np.ones((4,4))
print(a)

'''



























































































