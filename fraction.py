def gcd(m,n):
        while m%n !=0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n

class fraction:
    def __init__(self,top,bottom):
        self.numerator = top
        self.denominator = bottom
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    def show(self):
         print(f"{self.numerator}/{self.denominator}")
    
        
    def __add__(self, other_fraction):
        new_denominator = self.denominator * other_fraction.denominator
        new_numerator =  self.numerator*other_fraction.denominator + self.denominator*other_fraction.numerator
        
        common = gcd(new_numerator,new_denominator)
        return fraction(new_numerator//common,new_denominator//common)
# my_f = fraction(3,5)
# print(my_f)
# print(f"I am hungry for {my_f} hours.")
# print(my_f.__str__())
# print(str(my_f))
 
f1=fraction(1,4)
f2=fraction(1,2)
f3= f1+f2
print(f3)
print(f1==f2)
