#modifying using slice method 
'''tup=(1,2,3,4,5,6,7)
print("normal tuple ",tup)
modified_tup=tup[2:]+(100,500)+tup[3:]
print(modified_tup)'''

#modifying using list
tup1=(1,2,3,4,5,6,7,8)
print("before converting ",tup1)
tup_list=list(tup1)
print("after convert to list ",tup_list)
tup_list[3]=100
tup_list[2]=1000
print(tup_list)
modified_tup=tuple(tup_list)
print(modified_tup)
