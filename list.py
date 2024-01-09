list=["aiman",1,1.3,True]
print(list)
#display list using for
for i in list:
    print(i,end=" ")

#accsessing list using index
print()
print(list[0])
print(list[-1])
print()
#modifying list
print("before modifying list ",list)
list[3]="hello"
print("After modifying ",list)