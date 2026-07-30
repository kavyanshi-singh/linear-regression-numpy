import numpy as np

a=np.array([[10,20,30], [40,50,60]])
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(b.ndim)
print(b[0,:1])
print(b[1,0,2])
print(b[0,1:3])

x=np.array([1,2,3,4])     #add
y=np.array([5,6,7,8])
z=np.add(x,y)
print(z)

x=np.array([1,2,3])       #multiply
y=np.array([4,5,6])
z=np.multiply(x,y)
print(z)

x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.divmod(x,y)
print(z)

x=np.array([1,2,3,4,5,6])
y=x.reshape(2,3)
print(y)