#getting input from user in list
list=[]
n=int(input('Enter numbers of elemnst you want to enter '))
for i in range(n):
    list.append(input("Enter elements "))
print("Your elements are  ",list)

#accsessing using for loop
print("-------accsessing using for loop--------")
for i in list:
    print(i)
