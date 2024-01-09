#takes one function and one or more iterable as arguments and return the filtered iterable 
#filter using normal function
'''print('---return the value greater than 3 in list using normal function----')
l=[1,2,3,4,5,6]
def greater(i):
    return i>3
result=list(filter(greater,l))
print(result)'''

#filter using normal lamba function
#finding even in list using lamba function
'''print("----finding even in list using lamba function-------")
l2=[1,2,3,4,5,6,7]
even=list(filter(lambda x:x%2==0,l2))
print("even in list are ",even)'''
#finding non-empty string using filter in lamba
'''l3=["","aiman","","ansari"]
non_empty=list(filter(lambda element:len(element)>0,l3))
print("non empty words are ",non_empty)'''
print('---- Using Null in filter() ------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [True,False,True,False,True]

even_numbers = list(filter(None, numbers))
print(even_numbers)

print()
