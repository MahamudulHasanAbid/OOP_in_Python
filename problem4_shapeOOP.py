class Shape:
    
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r

    def area(self, pi=3.1416):
        self.pi = pi

        Area = self.pi * self.r * self.r
        return Area
    def perimeter(self, pi =3.1416):
        Perimeter = 2* self.pi * self.r
        return Perimeter
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2* (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, s1, s2, s3):
        self.base = base
        self.height = height
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.s1 + self.s2 + self.s3

print('circle:')
circle = Circle(3)
print(f" Area: {circle.area()}")
print(f" Perimeter: {circle.perimeter()}")

print('rectangle:')
rectangle = Rectangle(5,9)
print(f" Area : {rectangle.area()}")
print(f" perimeter : {rectangle.perimeter()}")
print('triangle:')
triangle = Triangle(3, 4, 3, 5, 5)
print(f" Area: {triangle.area()}")
print(f" Perimeter: {triangle.perimeter()}")