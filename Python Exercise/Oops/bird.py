class Bird():
    def __init__(self,name):
        self.name = name
        self.does_fly = False
        
    def get_dtl(self):
        print('-----------------------------------------')
        print('From Parent Class')
        print(f'{self.name} can fly {self.does_fly}')
        print('-----------------------------------------')

class Test1(Bird):
    # def __init__(self):
    #     super(Bird, self).__init__()
        
    
    def get_dtl(self):
        self.does_fly = True
        print('From Child Class')
        print(f'{self.name} can fly {self.does_fly}')
        print('-----------------------------------------\n')


B1 = Bird('ostrice')
B1.get_dtl()
# B2 = Bird('Parrot')
# Test1.get_dtl(B2)
B2 = Test1('Parrot')
Test1.get_dtl(B2)
