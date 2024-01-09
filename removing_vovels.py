str=input("Enter string :")
vovels=['a','e','i','o','u','A','E','I','O','U']
result=""
for i in str:
    if i not in vovels:
     result=result+i
     

print("after removing vovels ",result)