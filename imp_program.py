'''#prime
num=int(input("Enter a number "))
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("Enter valid number")'''

'''#fact
num1=int(input("Enter a number"))
fact=1
if num1<0:
    print("Enter valid num")
elif num1==0:
    print("Enter valid num")
else:
    for i in range(1,num1+1):
        fact=fact*i
    print("factorial of ",num1," is ",fact)'''

'''#leap
year=int(input('Enter a year '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print('leap year')
else:
    print('not leap year')'''

#palingdrome
str=input("Enter something ")
if str==str[::-1]:
    print('palingdrome')
else:
    print('not palingdrome')