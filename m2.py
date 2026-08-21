class Rectangle:
    """To'rburchak hisob kitob"""
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        
    def get_hight(self):
        return self.hight
    
    def set_hight(self, h):
        self.hight = h
    
    def get_width(self):
        return self.width
    
    def set_width(self, w):
        self.width = w
        
    def get_area(self):
        return self.hight * self.width
    
    def get_perimeter(self):
        return 2 * (self.hight + self.width)
    
    def get_info(self):
        print(f"hight: {self.hight}")
        print(f"width: {self.width}")
        print(f"Area: {self.get_area()}")
        print(f"Perimeter: {self.get_perimeter()}")

rectangle1 = Rectangle(4, 5)
rectangle1.get_info()
rectangle1.set_hight(10)
rectangle1.set_width(15)
rectangle1.get_info()