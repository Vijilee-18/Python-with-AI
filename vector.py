import numpy as np
vector1=np.array([2,3,4])
for i in vector1:
    if i%2==0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
