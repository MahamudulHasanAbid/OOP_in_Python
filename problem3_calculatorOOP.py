class calculator:
    def __init__(self, *args):
        self.values = args

    def add(self):
        return sum(self.values)
    def sub(self):
        result = self.values[0]
        for i in self.values[1:]:
            result -= i
        return result
    
    def mul(self):
        result = self.values[0]
        for i in self.values[1:]:
            result *= i
        return result        

    def divi(self):
        result = self.values[0]
        if 0 in self.values[1:]:
            raise ValueError("zero is not allowed for dinominator")
        result = self.values[0]

        for i in self.values[1:]:
            result /= i

        return result
    
perform = calculator(2,3,5)

perform_add = perform.add()
print(f"{perform_add}")

perform_sub = perform.sub()
print(f"{perform_sub}")

perform_mul = perform.mul()
print(f"{perform_mul}")

divis = calculator(9,5)
perform_divi = divis.divi()
print(f"{perform_divi}")