#Without using numpy

listA=[1,2,3,4]
listB=[]
for i in listA:
    listB.append(i+10)
print(listB)

'''With numpy . Here Broad Casting is used.'''

import numpy as np
vectorA=np.array([1,2,3,4])
print(vectorA+10)

