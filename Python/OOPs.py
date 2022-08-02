import math

class Point: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_calcualte(self, pointB):
        x1 = self.x
        y1 = self.y
        x2 = pointB.x
        y2 = pointB.y

        result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        print(f"The distance between points is {result} units")
    
    def __str__(self):
        return f'New Coordinate is {self.x,self.y}'

P1 = Point(2, 3)
P2 = Point(6, 6)
P1.distance_calcualte(P2)

P3 = Point (4,5)
print("This is str.", P3)