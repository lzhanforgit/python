import numpy as np
narr1=np.array([1,2,3])
narr2=np.array([[1,2,3],[4,5,6]],ndmin=3)
narr3=np.array([[1,2,3],[4,5,6]],dtype=float)
narr4=np.array([3,2,5],order="F")
print(narr1)
print(narr2)
print(narr3)
print(narr4)

num1=np.array([1,2,2],dtype=np.float)
print(num1)

print(np.dtype(np.int32))