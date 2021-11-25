"""
Fill in the class
"""


class Cylinder:
    PI = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.PI * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * self.PI * self.radius * (self.height + self.radius)


if __name__ == '__main__':
    c = Cylinder(2, 3)
    print(c.volume())
    print(c.surface_area())