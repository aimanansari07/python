num=int(input('Enter a number'))
fact=1
if num<0:
    print('Enter valid number')
elif num==0:
    print('Enter valid number')
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,'is ',fact)
      