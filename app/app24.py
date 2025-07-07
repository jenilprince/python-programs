import numpy as np
p=np.array([1,2,3])
print(p)
p1=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,0]
])
print(p1)
print(np.zeros((3,6),int))
print(np.arange(0,21,4))
print(np.linspace(1,100,100))
print(p1.shape)
print(p1.ndim)
print(p1.size)
print(p1.dtype)
print(p1[:,0])
print(np.matmul(p,p1))
