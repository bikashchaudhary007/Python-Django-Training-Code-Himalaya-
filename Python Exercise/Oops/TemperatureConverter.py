'''
Create a TemperatureConverter class, where you need to convert between Kelvin , celsius and Fahrenheit . 
Eg: if degree is given in C, a method to convert C to K, and another to C to F.

Similarly, do for all three temperature measuring units. Hint: use static methods
'''
class TemperatureConverter():
    def __init__(self, celsius):
        pass 
    
    @staticmethod
    def celsius_to_fahrenheit():
        celsius_val = float(input("Enter the value to celsius degree: "))
        fahrenheit_val = (9/5*celsius_val)+32
        print(f'The converted temperature value:\n {celsius_val} degree celsius = {fahrenheit_val} degree farenheit')
    
    @staticmethod
    def fahrenheit_to_celsius():
        fahrenheit_val = float(input("Enter the value of degree farenheit: "))
        celsius_val = (5/9)*(fahrenheit_val-32)
        print(f'The converted temperature value:\n {fahrenheit_val} degree farenheit = {celsius_val} degree celsius')
    
    @staticmethod
    def celsius_to_kelvin():
        celsius_val = float(input("Enter the value of degree celsius: "))
        kelvin_val = celsius_val + 273
        print(f"The converted temperature value:\n {celsius_val} degree celsius = {kelvin_val} K")
    
    @staticmethod
    def kelvin_to_celsius():
        kelvin_val = float(input("Enter the value of kelvin: "))
        celsius_val = kelvin_val - 273
        print(f'The converted temperature value:\n {kelvin_val} K = {celsius_val} degree celsius')


TemperatureConverter.celsius_to_fahrenheit()
TemperatureConverter.fahrenheit_to_celsius()
TemperatureConverter.celsius_to_kelvin()
TemperatureConverter.kelvin_to_celsius()


        
