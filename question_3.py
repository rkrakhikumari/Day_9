class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side )

Rectangle = rectangle(12, 8)
print(f"area of rectangle: {Rectangle.area()}")
print(f"perimeter of rectangle:{Rectangle.perimeter()}")
Square = square(10)
print(f"area of square:{Square.area()}")
print(f"perimeter of sqaure:{Square.perimeter()}")

