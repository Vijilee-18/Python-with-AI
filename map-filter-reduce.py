#Performing the use of Functions like map(),filter(),reduce()#
#map functions

list_1=[2,4,56,7,90]
var=list(map(lambda x:x**2,list_1))
print(f"Square of each element of the list is:{var}")

#filter functions

list_2=[1,2,3,4,5,6,7,8,9,10]
var_2=list(filter(lambda x:x%2!=0,list_2))
print(f"Odd number in the list is :{var_2}")

#reduce function#
from functools import reduce
list_3=[1,2,3,4,5]
var_3=reduce(lambda x,y:x+y,list_3,0)
print(f"The sum of the list is :{var_3}")
