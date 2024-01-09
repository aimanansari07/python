#The hasattr() function returns True if the specified object has the specified attribute, otherwise False
class Demo:
    name="Aiman"
    age=22
    salary=5000000
    print(name,age,salary)
print(hasattr(Demo,"age"))
#d=Demo()