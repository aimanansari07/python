#reduce takes iterable object but return only one result
#multiplication of numbers in list using lamba in reduce
print("-----------multiplication of numbers in list using lamba in reduce-------")
from functools import reduce
l=[1,2,3,4,5,6]
res= reduce(lambda x,y:x*y,l)
print("multiplication of list is ",res)
print(type(res))
