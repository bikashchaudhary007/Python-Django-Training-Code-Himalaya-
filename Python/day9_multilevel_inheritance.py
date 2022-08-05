class First():
    def __init__(self) -> None:
        print("This is first init")
    
    def testing_method(self):
        print("First Method")

class Second(First):
    def __init__(self) -> None:
        super(Second,self).__init__()
        print("This is second init")
    
    def testing_method(self):
        print("Second Method")

class Third(Second):
    def __init__(self) -> None:
        super(Third,self).__init__()
        print("This is third init")

    def testing_method(self):
        print("Third Method")

third = Third()
print(Third.mro())
print(third.testing_method())