"""
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""
from math import sqrt

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


if __name__ == '__main__':
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    line = Line(coordinate1, coordinate2)

    print(line.distance())
    print(line.slope())