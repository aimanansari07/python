#defualt arguments
#example 1
def default(a=20,b=10):
    print("addtion of two number is  ",a+b)
default()
#example 2
def names(fname='Aiman',lname='Ansari'):
    print('my name is ',fname,lname)
names('tony')
print()
#keyword arguments(in this argument order of arguments is not matter)
#example 1
print("-----------keyword arguments------------------")
def keyword(b=9,a=10):
    print("subtraction of two numbers is ",a-b)
keyword(b=10,a=5)
#example 2
def keyword2(lname,fname):
    print('full name is ',lname,fname)
keyword2(fname='aiman',lname='ansari')
print()

#required arguments(in this argument its compulsory to pass value in arguments)
#exampple 1
print("----------required arguments--------")
def reqiured(a,b=6):
    print("multiplication of two numbers is ",a*b)
reqiured(3)
#example 2
def keyword2(lname,fname='aiman'):
    print('full name is ',lname,fname)
keyword2('ansari')
print()

#variable lenght arguments(if we put single * it will take values in tuples)
#taking values in tuples because its single *
print("-------variable lenght arguments--------")
def variable_len(*names):
    print(type(names))
    print("all names is ",names)
    for i in names:
        print(i,end=" ")
variable_len('Aiman','tony','steve','strange')

#taking values in dictonary{key:value} because its ** 
'''def variable_len2(**info):
    print("informations are ",info)
variable_len2('name':'ansari')'''


