# Encapsulation is about binding data and function together. Can not access directly from the outside of the class. But we 
#can access using in a controlled manner. which is given below. It means encapsulation is also for the controlling of data.

class rice:

    def __init__(self):
        self.__maxprice = 70

    def sell(self):
        print(f"The price of nazirshile is {self.__maxprice} BDT")

    def setprice(self,price):
        self.__maxprice = price

nazir = rice()
nazir.sell()

print("\n")
nazir.__maxprice = 90   #Can not change the value, cause __maxprice is a private variable, is responsible for encapsulation
nazir.sell()

print("\n")
nazir.setprice(80)
nazir.sell()