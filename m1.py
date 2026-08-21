from math import pi

class Circle:
    """aylana hisob kitob klassi"""
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def get_radius(self):
        return self.radius
    
    def set_radius(self, r):
        self.radius = r
    
    def get_color(self):
        return self.color
    
    def set_color(self, c):
        self.color = c
        
    def get_area(self):
        return pi * pow(self.radius, 2)
    
    def get_cirumference(self):
        return 2 * pi * self.radius
    
    def get_info(self):
        print(f"Radius: {self.radius}")
        print(f"Color: {self.color}")
        print(f"Area: {self.get_area():.1f}")
        print(f"Cirumference: {self.get_cirumference():.1f}")
        
circle1 = Circle(4, "Red")
circle1.get_info()
circle1.set_radius(10)
circle1.set_color("Blue")
circle1.get_info()
    