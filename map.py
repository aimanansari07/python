#normal function
'''cube=[1,2,3,4,5]
def cube():
    for i in cube:
        print(i*i*i,end=" ")
cube()'''

#map takes one function and one or more iterable as arguments and return the iterable
#map using normal function
'''num=[1,2,3,4,5,6]
def square(s):
    
    return s**2
square=list(map(square,num))
print("sqaure is ",square)'''

'''result=list(map(square,num))
print(result)
#map using lamba function
print("map using lamba function")
num1=[1,2,3,4,5,6]
lamb_result=list(map(lambda x:x*2,num1))
print(lamb_result)'''

print('----- Squaring A Number Using Lambda function in map() Function With Two Argument -----')
'''num2=[1,2,3,4,5,6]
num3=[1,2,3,4,5,6]
result1=list(map(lambda x,y:x*y,num2,num3))
print(result1)'''
#check the particular elemnt present in string or not using lamba in map
str="aiman"
res=map(lambda i: i in str,str)
res(res)