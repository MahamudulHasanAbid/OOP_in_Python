import datetime
class person:
    
    def __init__(self, name, country, dob):
        self.name=name
        self.country = country
        self.dob = dob
    
    def add_age(self):
        today = datetime.date.today()
       
        age = today.year - self.dob.year-((today.month, today.day)<(self.dob.month, self.dob.day))
        return age
    
    def show(self):
        age = self.add_age()
        print(f"This is {self.name} \nCountry: {self.country} \nDate Of birth:{self.dob} \nage: {age}")


Person = person('Abid', 'Bangladesh', datetime.date(1998, 4, 19))
Person.show()

    