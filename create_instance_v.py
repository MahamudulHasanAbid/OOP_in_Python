'''Create instance variable.
***Instance variable are the value of variable varies from object to object.***
***We can dynamically add instance variable to the object.***
'''
class info:
    #defining a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = info('abid', 25) 

s2 = info('Hasan', 24)
# s1, s2 are the objects of info 
print(f"{s1.name} is {s1.age}")  #Achieving instance variable using object(s1) and .(dot) operator
print(f"{s2.name} is {s2.age}")

# Dynamically adding instance variable:

s1.id = '001A'
s2.id = '001C'

print(f"Name:\t {s1.name} \nID :\t {s1.id} \nage:\t {s1.age}")
print(f"Name:\t {s2.name} \nID :\t {s2.id} \nage:\t {s2.age}")

#Same way we can delete instance variable using 'del' keyword and 'delattr(object, name)' function.