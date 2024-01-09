tup=[]
num=int(input("Enter numbers of elements "))
for i in range(num):
    tup.append(input("Enter elements "))

#print("elements are ",tup)
tup1=tuple(tup)
print("elements are ",tup1)