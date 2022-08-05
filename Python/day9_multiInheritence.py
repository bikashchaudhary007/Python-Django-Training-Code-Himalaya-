class First(object):
    def __init__(self):
        # super(First, self).__init__()
        print("first")
    
    def test():
        print("First Method")

class Second(object):
    def __init__(self):
        print("Second")
    def test():
        print("second method")

class Third(First, Second):
    def __init__(self):
        super(Third,self).__init__()
        print("Third")
    def test():
        print("This is 3rd method")

print("--------------------------------------------------------")
Third()
print(Third.mro())
print(Third.test())