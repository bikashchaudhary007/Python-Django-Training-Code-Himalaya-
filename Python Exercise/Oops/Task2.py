'''
Create a class Point where initial x,y values are initialized with 0. 
Create objects of class Point with x and y values passed to it. 

Eg: point p1 with x=2 and y=3 should be created.
		
Create a method to Calculate distance between two points. 

Formula: res = sqrt((x2-x1)^2 + (y2-y1)^2)   , where x1 and x2 are x values of p1 and p2 points resp. , y1 and y2 are y values of p1 and p2 resp.

Represent the point objects with x, y values in the format: (x,y). Eg: (2,3).

'''
import math
class Distance:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_values(self):
        print(f'Coordinates: (x,y) = ({self.x},{self.y})')


P1 = Distance(x=2, y=3)
P2 = Distance(x=6, y=6)
P1.get_values()
P2.get_values()

def distance_between():
    
    result = math.sqrt((P2.x-P1.x)**2 + (P2.y-P1.y)**2)
    print(f"The distance between points is {result} units")

distance_between()

