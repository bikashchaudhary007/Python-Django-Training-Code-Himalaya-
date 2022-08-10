from abc import ABC,abstractmethod

class Car(ABC):
    
    @abstractmethod
    def test_drive(self):
        pass

# c = Car()

class BMW(Car):

    def test_drive(self):
        print("BMW car")

B1 = BMW()
B1.test_drive()
