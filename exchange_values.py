#with temp variable
num1=10
num2=20
temp=num1
num1=num2
num2=temp
print("number 2 value is ",num2)
print("number 1 value is ",num1)

#without temp variable
num1=30
num2=20
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)
