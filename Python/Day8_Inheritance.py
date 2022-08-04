'''

'''
class vehicle():
    def __init__(self,name, model, brand, color):
        self.name = name
        self.model = model
        self. brand = brand
        self.color = color
    
    def get_vehicleDetails(self):
        print(f'Vehicle Details:\n name: {self.name}\n model: {self.model}\n brand: {self.brand}\n color: {self.color}')

v1 = vehicle('Tesla-X', 'Ten-X', 'Tesla', 'Silver')
v1.get_vehicleDetails()

class vehicleChanges(vehicle):
    def changeColor(self):
        self.color = color

v1_C = vehicleChanges('Tesla-X', 'Ten-X', 'Tesla', 'Red')
# print(v1_C.get_vehicleDetails())
v1_C.get_vehicleDetails()

print(vehicleChanges.mro()) #defines the order of the methods calling

