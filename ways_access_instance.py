'''Ways to access instance variable 
* There are two ways to access instance variable.
    1.Using OBJECT_REFERENCE which is 'self' 
    2. Using getattr() method.
'''

#Access using 'self':

class Biriyani:
    def __init__(self, ingridient, amount, name):
        self.ingridient = ingridient
        self.amount = amount
        self.name = name
    def show(self):
        print(f"{self.ingridient} is required {self.amount} for {self.name}" )   #Using object reference.

tehari = Biriyani('rice and meat', '1:1', 'tehari')
tehari.show()

Kacchi = Biriyani('rice and mutton', '1:2', 'Kacchi')
Kacchi.show()

#Access using 'getattr()

class Food:
    def __init__(self, name, category):
        self.name = name
        self.category = category

rice = Food('rice', 'staple/Crop')
Potato = Food('Potato', 'staple/Vegitable')
tomato = Food('tomato', 'vegitable')

# Both the way is given below... 
print(f"Name of food is {Potato.name} and category is",getattr(Potato,'category'))
print(f"Name of food is {tomato.name} and category is",getattr(tomato,'category'))
print(f"Name of food is {rice.name} and category is",getattr(rice,'category'))    




