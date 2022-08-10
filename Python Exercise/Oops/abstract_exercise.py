from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def bird_name(self):
        pass
    
    @abstractmethod
    def does_fly(self):
        pass

    @abstractmethod
    def does_migrate(self):
        pass

    @abstractmethod
    def how_far(self):
        pass

class Bird_Bav(Bird):
    def __init__(self,name,fly,migrate,far):
        self.name = name
        self.fly = fly
        self.migrate = migrate
        self.far = far

    def bird_name(self):
        print(f'name: {self.name}')

    def does_fly(self):
        print(f'does fly: {self.fly}')
    
    def does_migrate(self):
        print(f'does migrate: {self.migrate}')
    
    def how_far(self):
        print(f'how far: {self.far}')

B1 = Bird_Bav('Parrot','Yes', 'Yes','200km')
B1.bird_name()
B1.does_fly()
B1.does_migrate()
B1.how_far()
