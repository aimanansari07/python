class Duck:
    def speak(self):
        print('Quek!!')
class Cat():
    def speak(self):
        print("Meow!!")
def Voice(Animal):
    Animal.speak()
d=Duck()
c=Cat()
Voice(d)
Voice(c)