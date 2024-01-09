#deleting entire tuple using del keyword
'''tup=(1,2,3,4,5,6,7,8,9)
print(tup)
del tup
print(f'after deleting {tup}')
'''
#deleting  tuple elements by converting in list
tup2=(1,2,3,4,5,6,7,8,9)
list_tup=list(tup2)
print("After convert into list ",list_tup)
list_tup.remove(5)
print(list_tup)
tup_list=tuple(list_tup)
print(tup_list)