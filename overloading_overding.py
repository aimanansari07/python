#method overloading
'''class Parent:
    def cal(self,a,b):
        mul=a*b
        print("mul is ",mul)
class Child(Parent):
    def cal(self, a, b,c=10):
        add=a+b+c
        super().cal(4,4)
        print('addtion is ',add)
c=Child()
c.cal(10,2)'''
#method overriding
class Parent:
    def cal(self,a,b):
        sub=a-b
        print('subtraction is ',sub)
class Child(Parent):
    def cal(self,a,b):
        add=a+b
        print("Addition is ",add)
        super().cal(50,20)
c=Child()
c.cal(20,5)
