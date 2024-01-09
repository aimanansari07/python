#prorgam that counts the number of elements in list with value greater than 3
l1=[1,2,3,4,5,6,7,8,9]
Res=[]
for i in l1:
          if i>3:
                  Res.append(i)
print(Res)
print("the final count is ",len(Res))

'''l2=[[1,2,3],[4,5,6],[7,8,9]]
l3=[]
for i in range(len(l2)):
          l3+=l2[i]
print(l3)
 '''
# covert this [[1,2,3],[4,5,6],[7,8,9]] to this [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
for i in l2:
          for j in i:
                  res.append(j)
print(res)

#second largest elements in list
l3=[]
num=int(input("Enter number of elemnts "))
for i in range(num):
        l3.append(input('Enter integer elemnts ' ))

s=set(l3)
l=list(s)
print("second largest elemnt is ",l[-2])