#Inheritance is a way of creating a new class for using the details of an existing class.
#It means whenever there will be some common thing in different classes we will be able to declare those thing in a single class and later on we will be able to call that class in an another class

#Here 'Polymorphism' also occured in the code. we can see that we have used study() function for different class.
#Also eat() and sleep() function has been used for both Human and Bird class as inherited data.
class Animal:
    def eat(self):
        print("Every animal eats.")
    def sleep(self):
        print("Every animal sleeps.")

class Human(Animal):
    def study(self):
        print("Only we do study.")

class Bird(Animal):
    def fly(self):
        print("Only birds can fly.")
    def study(self):
        print(f"We do not study.")

human=Human()  #human=object
human.eat()
human.sleep()
human.study()
print("\n")
bird = Bird() #bird is the object
bird.eat()
bird.sleep()
bird.fly()
bird.study()