class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2
circle=circle(14)
print("area of the circle is",circle.area())