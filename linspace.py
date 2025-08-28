'''linspace():Used to create an evenly spaced values
 syntax:linspace(start,stop,num,endpoint,retstep)
 start:It is the Starting value
 Stop:It is the Ending Value
 num:it is the amount of numbers coming between the start and end value
 endpoint:Using this we get the endpoint of the sequence typically the stop value
 retstep:Using this we the get the value which is used to divide the number's between the start and stop value. Typically the common
         difference.
 endpoint,retstep is optional while initializing.'''
import numpy as np
var=np.linspace(0,100,5,endpoint=True,retstep=True)
print(var)