"""
This is circle module which has Circle Class with  two method
1. area #which compute the area of circle
2. perimeter # which compute the perimeter of circle, 

"""
#import value of pi from math module 
from math import pi

class Circle(object):
    """
    This is Circle class which has two method
    1. area #which compute the are of circle
    2. perimeter #which compute the perimeter
    
    """
    #initilize circle with diameter 
    def __init__(self, diameter):
        
        self.diameter = diameter
    def area(self):
        """
        Compute  and Return area of circle with given diameter.
        """
        area = pi*(self.diameter**2)/4
        #return result with roundup 4 digits
        return round(area, 4)
    
    def perimeter(self):
        """
        Compute and Return perimeter of circle with given diameter.
        """
        perimeter = self.diameter*pi
        #return result with roundup 4 digits
        return round(perimeter, 4)

#This will execute when mudule is directly run from command line.
if __name__=="__main__":
    diameter = input("Enter the diameter of a circle: ")#diameter input 
    c = Circle(diameter) #create circle object c
    print(c.area()) #print the are of the circle
    print(c.perimeter()) #print the perimeter of the circle
    
    
