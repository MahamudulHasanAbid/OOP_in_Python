class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):     #instance method
        pi = 3.1416
        Area =  pi * self.r * self.r   
        return Area
    def perimeter(self):   #instance method
        pi=3.1416
        Peri= 2*pi*self.r
        return Peri 
    def show(self):
        print(f"Area of Circle is : {self.area()} \nPerimeter of Circle is: {self.perimeter()}")    

value_of_radius = int(input("Enter a radius value to calculate: "))
circle = Circle(value_of_radius) 
circle.show()

# print(circle.area())
# print(circle.r)
# print(circle.perimeter())
        