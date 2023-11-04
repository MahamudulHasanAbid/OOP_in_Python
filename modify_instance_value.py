class info:
    # __init__ is a  constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = info('Thor', 70)
s2 = info('Tony', 60)

print(f"{s1.name} is {s1.age}")

s1.name = "Hulk"          # We can modify instance variable through this types of line. 
print(f"{s1.name} is {s1.age}")

print(f"{s2.name} is {s2.age}")
s2.age = 55
print(f"No no {s2.name} is {s2.age}")