#encapsulation have three type 
#public
#private
#protected

#public
'''class Base:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
       

    def display(self,location):
        self.location=location
        print(f"Name is {self.name} age is {self.age} and location is {self.location}")

class Derived(Base):
    pass

d=Derived("aiman",22)
d.display("mumbai")
print("----Accessing public variable outside the class----- ")
print(f"name is {d.name} ")'''

#protected
'''class Base:
    def __init__(self,name,age) -> None:
        self._name=name #protected vairable
        self._age=age #protected vairable

       

    def display(self,location):
        self.location=location
        print(f"Name is {self._name} age is {self._age} and location is {self.location}")

class Derived(Base):
    pass

d=Derived("aiman",22)
d.display("mumbai")
print("----Accessing protected variable outside the class----- ")
print(f"name is {d._name} ")
d._name="Ansari"
print(f"After update the name {d._name} ")
print(f"Name is {d._name} age is {d._age} and location is {d.location}")'''

#private
class Base:
    def __init__(self,name,age) -> None:
        self.__name=name #private variable
        self.__age=age #private variable
       

    def display(self,location):
        self.location=location
        print(f"Name is {self.__name} age is {self.__age} and location is {self.location}")



b=Base("aiman",22)
print("--- Acess private variable by calling method---")
b.display("mumbai")
print("----Accessing private variable outside the class----- ")
print(f"name is {b._Base__name} ") #namemangling