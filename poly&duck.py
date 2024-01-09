#duck typing
class Duck:
    def sound(self):
        print('quek quek!!')
class Dog:
    def sound(self):
        print("Bhow Bhow!!")
class Cat:
    def sound(self):
        print("Meow Meow!!")
def Voice(obj):
    obj.sound()
d=Duck()
Voice(d)
d=Dog()
Voice(d)
c=Cat()
Voice(c)