#function without parameter
def hello():
    print("hello world")
hello()

'''def sum():
    num1=int(input("enter first number "))
    num2=int(input("enter second number "))
    res=num1+num2
    print("Addition of two number is  ",res)
sum()'''

#function with parameter
name="aiman"
def names(name):
    print("my name is ",name)
names(name)

#addtion of two numbers using passing parameter in function

def add(x,y):
    result=x+y
    print("Addition is " ,result)
add(10,5)
print()

# Defining multiple function and callling in one function
print("Defining multiple function and callling in one function")
print()
def addition(x,y):
    result=x+y
    print("addition is ",result)

def sub(x,y):
    result=x-y
    print("subtraction is ",result)

def mul(x,y):
    result=x*y
    print("multiplication is ",result)

def calculate():
    addition(10,20)
    sub(10,5)
    mul(10,5)
calculate()

