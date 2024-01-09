'''#Q1.Write a program to compare two numbers and print whether they are equal or not.
a=10
b=20
if(a==b):
    print("equal")
else:
    print("not equal")

#Q2.Create a program that checks whether a given number is positive, negative, or zero
a=10
if(a>0):
    print("positive")
elif(a<0):
    print("negative")
elif(a==0):
    print("zero")

#Q3.Write a program to compare three numbers and find the maximum among them.
a=100
b=20
c=30
if(a>b):
    print(a,"is greater")
elif(b>c):
    print(b,"is greater")
else:
    print(c,"is greater")

#Q4.Create a program to determine if a given year is a leap year or not.
year=int(input('Enter a year '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")'''

#Q5.Write a program to compare two strings and check if they are equal or not.
'''str1="aiman"
str2="Aiman"
if str1==str2:
    print("equal")
else:
    print("not equal")'''
#Q6.Create a program to determine whether a given number is even or odd.
'''a=100
if(a%2==0):
    print("even")
else:
    print("odd") '''
#Q7.Write a program to check if a number is positive and even.
'''a=100
if (a>0 and a%2==0):
    print("positive and even")
else:
    print("negative or odd")'''

#Q8.Create a program to check if a number is divisible by another number.
'''b=20
num=2
if (b%num==0):
    print("divisible")
else:
    print("not divisible")'''
#Q9.Write a program to check if a given character is a vowel or consonant.
'''vowels=['a','e','i','o','u','A','E','I','O','U']
char=input('Enter character ')
if (char in vowels):
    print("vowel")
else:
    print("consonant")'''
#Q10.Create a program to check if a number is greater than, less than, or equal to zero
'''b=20
if(b>0):
    print("greater than zero")
elif(b<0):
    print("less than zero")
else:
    print("equal to zero ")'''
#Q11.Create a program to check if a number is positive and greater than 10.
b=20
'''if (b>0 and b>10):
    print(b,"is positive and greater than 10 ")
else:
    print(b,"number is negative or less than 10")'''

#Q12.Write a program to check if a number is odd and less than 100
b=201
if (b%2!=0 and b<100):
    print(b,'is odd or less than 100')
else:
     print(b,'is even or greater than 100')