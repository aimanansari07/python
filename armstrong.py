'''num=1634
str_num=str(num)
l=len(str_num)
sum=0
for i in str_num:
    r=int(i)**l
    sum=sum+r
if num==sum:
    print("armstrong")
else:
    print("not armstrong")'''

x=int(input("Enter the Number : "))
for num in range(1,x+1):
    str_num=str(num)
    l=len(str_num)
    res=0
    for i in str_num:
        r=int(i)**l
        res+=r
    if num==res:
        print(num)

