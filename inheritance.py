#single inheritance
'''class Parent:
    def __init__(self) -> None:
        print("This is parent classs")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class ")
c=Child()'''
#multilevel inheritance
'''class GrandFather:
    def __init__(self) -> None:
        print('Granfather ')
class Father(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print('Father ')
class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print('Son')
s=Son()'''

#multiple inheritance(that contains 2 parent class and 1 child class)
'''class Dad:
    def __init__(self) -> None:
        super().__init__()
        print("Class Dad")
class Mom:
    def __init__(self) -> None:
        super().__init__()
        print('Class Mom ')

class Child(Dad,Mom):
    def __init__(self) -> None:
        super().__init__()
        print('Class Child ')
c=Child()   
'''
#Heirarchical Inheritence(Single parent but multiple child)
'''class Parent:
    def __init__(self) -> None:
        print("Parent Class ")
class Brother(Parent):
    def __init__(self) -> None:
        super().__init__()
        print('Brother Clss ')
    def Brother_prop(self):
        print('Brother Property')

class Sister(Parent):
    def __init__(self) -> None:
        super().__init__()
        print('Sister class')
    def Sister_prop(self):
        print('Sister Property')
b=Brother()
b.Brother_prop()
s=Sister()
#s.Brother_prop()'''
# First product method.
# Takes two argument and print their
# product


def product(a, b):
	p = a * b
	print(p)

# Second product method
# Takes three argument and print their
# product


'''def product(a, b, c):
	p = a * b*c
	print(p)'''

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4,7)
