#Q1. Create a program that takes two numbers as input and prints their sum.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print("Addition is ",n1+n2)'''
'''Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
'''
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print("Subtraction  is ",n2-n1)'''
#Q3.Create a program that multiplies two numbers taken as input.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print("Multiplication   is ",n1*n2)'''
#Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print("Division   is ",n1/n2)'''
#Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print("Floor Division   is ",n1//n2)'''
#Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print(" remainder  is ",n1%n2)'''
#Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.
'''n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
print(" Exponential is  is ",n1**n2)'''
#Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
'''p=float(input("Enter principal amount "))
roi=float(input("Enter  rate of intrest "))
t=int(input("Enter time in years "))
ci=p*(1+roi/100)**t-p #formula to calculate ci
print(" Compound intrest  is ",ci)'''
#Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
#increment
'''n=int(input("Enter a number "))
for i in range(n):
    n=n+1
    print(n)'''
#decrement
'''n=int(input("Enter a number "))
for i in range(n):
    n=n-1
    print(n)'''
#Q10.Write a program that takes three numbers as input and calculates their average.
n1=int(input("Enter First number "))
n2=int(input("Enter  second  number "))
n3=int(input("Enter  third  number "))
avg=(n1+n2+n3)/3
print("Average is ",avg)