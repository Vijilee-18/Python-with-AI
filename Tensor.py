import numpy as np
#1 Dimension Tensor's:

tensor1=np.array([43,54,68])
print(tensor1)

#2 Dimension Tensor's:

tensor2=np.array([[1,2,3],[5,6,7]])
print(tensor2)

#3 Dimension Tensor's:

tensor3=np.array([[[9,8,7],[76,54,32]],[[34,54,67],[87,90,45]]])
print(tensor3)

#matrix multiplication:

tensorA=np.array([[2,3],[4,5]])
tensorB=np.array([[6,8],[9,10]])
result=np.dot(tensorA,tensorB)
print(result)