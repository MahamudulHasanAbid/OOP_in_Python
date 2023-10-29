'''1. Create a child class that will inherit all the variables and method of parent class.
2. Inherit by adding an extra argument in the child class'''
class vehichle:
    def __init__(self, name, speed, milage):
        self.name = name
        self.speed = speed
        self.milage = milage
    def seating_capacity(self, capacity):
        return capacity
class Bus(vehichle):
    def __init__(self, name, speed, milage,capacity=50):
        super().__init__(name, speed, milage)
        self.capacity = capacity
 
    def seating_capacity(self):
        return self.capacity
   

school_bus = Bus("Volvo", 200, 50)
print("\tVehichle Name:\t",school_bus.name, "\n\tTop speed:\t", school_bus.speed, "\n\tMilage:\t\t" ,school_bus.milage, "\nSeating capacity:\t" ,school_bus.seating_capacity())