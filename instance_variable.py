class Car:
    def __init__(self,color,model,Fuel) -> None:
        self.color=color
        self.model=model
        self.Fuel=Fuel
    def info(self,speed):
        self.speed=speed
        print(f"Car information is {self.color} {self.model} {self.Fuel}")
Bmw=Car("black",2022,"petrol")
Speed=Car.info(220)        
print("Speed of car is ",Speed)