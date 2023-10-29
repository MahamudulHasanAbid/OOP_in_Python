''' Create a class with instance attribute'''
class Vehicle:
   def __init__(self, max_speed=int, milage=int):
        self.max_speed = max_speed
        self.milage = milage

Bike = Vehicle(220, 12)
print(f"{Bike.max_speed} \t {Bike.milage}")
# print(str(Bike.max_speed)+ "\n" + str(Bike.milage))
