import numpy as np


#zad 11
print(np.arange(10, 100))


#zad 12
r12 = np.ndarray(shape=(9,10), dtype=int, buffer=np.arange(10,100))
print(r12)


#zad 13

r13 = np.eye(6,6, dtype = int)
print(r13)


np. random.seed(10)
r14 = np.random.rand(30)
print(r14)


#zad15

np. random.seed(20)
r15 = np.random.randn(10,4)
print(r15)


#zad16

np. random.seed(30)
sigma = np.sqrt(5)
m = 100
r16 = (sigma * np.random.randn(10,4) + m)
print(r16)


#zad17


A = np.array([[1, 4, 3],
              [5, 2, 6]])

for i in np.nditer(A):
    print(i)


#zad18

res18 = np.linspace(0, 1, num=11)
print(res18)


#zad19
np. random.seed(42)

res19 = np.random.choice(range(1,50), size=6, replace=False)
print(res19)


#zad20


print(np.diag(np.arange(6)))





































































