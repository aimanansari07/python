#prim number
num=int(input('Enter A number'))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print('This is not prime number')
            break
        else:
         print('this is prime number')
         break
else:
   print('Enter Valid number')