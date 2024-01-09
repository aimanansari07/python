s1={1,2,3,4}
s2={5,6,7,8,9}
#add method only add one element
print("------------add----------")
s1.add(5)
#s1.add(5,7) it gives an error
print(s1)
#remove it  show error if elemnt is not found
print("-------------remove-------")
s2.remove(9)
#s2.remove(944)
print(s2)
#update it will add multiple elemnt by using only iterable elemnt like list,tuple
print("------------update--------")
s1.update([5,6,7])
print(s1)
#discard will also remove elemnt but it doesnt show error if elemnt is not found
s1.discard(7)
s1.discard(9000)
print(s1)
#pop it will removes an random elemnts
print("------------------pop-------------")
s2={5,6,7,8,9}
print(s2)
s2.pop()
print("After pop ",s2)
s2.pop()
print("After pop ",s2)
#copy
print('-------copy--------------')
s1={1,2,3,4}
copy_set=s1.copy()
print("original set ",s1)
print("copy set ",copy_set)
copy_set.add(100)
print("original set ",s1)
print("copy set ",copy_set)
#clear it will remove all elements
print("---------clear------------")
print("before using clear method ",copy_set)
copy_set.clear()
print("After clear method ",copy_set)