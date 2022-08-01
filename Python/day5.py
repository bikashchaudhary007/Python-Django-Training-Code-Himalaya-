'''
Python Training 
Day 5

OOPs
'''
# class Person:
#     age = 19
#     name = "Bikash"

#     def get_name(self):
#         print(f'My name is {self.name}')

# p = Person()  #object person
# p2 = Person()
# p.get_name()

class person:
    def __init__(self, name="ABC", age = 32):
        self.age = age
        self.name = name
    
    def get(self):
        print('calling here: ',self.name, self.age)
    
    def __str__(self):
        return f'My name is {self.name}'


p = person()
print(p.age)
p2 = person(age = 19, name="Bikash")
print(p2.age, p2.name)

print(p.get())   # object le afno get call garyo with its own data
print(person.get(p2)) #class le get call gryo for which object vanera eg: p passes to it

print("This is str", p2)


