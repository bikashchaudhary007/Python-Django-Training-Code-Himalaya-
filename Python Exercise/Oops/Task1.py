'''
Create a class Vehicle with attributes: color, brand, vehicle_type (car, bike, truck, etc.), number_of_wheels (make default=4), price. Then create its object, along with a method to access its brand, vehicle type and price.
'''

class Vehicle:
    def __init__(self, color,brand, vehicle_type, number_of_wheels, price):
        self.color = color
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.number_of_wheels = number_of_wheels
        self.price = price

    def get_vehicle_details(self):
        print("Vehicle Details:-")
        print("Brand:",self.brand)
        print("Vehicle Type:",self.vehicle_type)
        print(f'Price: ${self.price}')

vehicle1= Vehicle(color="Red",brand="Tesla", vehicle_type="E-Car", number_of_wheels=4,price=15000)
vehicle1.get_vehicle_details()


