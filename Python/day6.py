from datetime import date
class Person:
    a = 5
    b = 6
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    @classmethod
    def obj_createwithage_by_yr(cls, name, year):
        age = date.today().year - year
        print("My age:",age)
        return cls(name, age)
    
    @classmethod
    def add_vals(cls):
        res = cls.a + cls.b
        print('res')
        return res

    
person = Person("Bikash",19)

p2 = Person.obj_createwithage_by_yr("Bikash", 2003)

result = Person.add_vals()
print(f"Sum of numbers is {result}.")

