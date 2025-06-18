class Shape:
    cnt = 0
    def __init__(self, color, isfill):
        self._color = color
        self.isfill = isfill
        Shape.cnt += 1
        
    def describe(self):
        print(f"this shape is {self._color} and it's {"filled" if self.isfill else "not filled"}")
        
    def say(self):
        print(f"this shape's saying something")
    
    @staticmethod    
    def is_shape(shape):
        shapes = ["circle", "square", "triangle"]
        return shape in shapes
    
    @classmethod
    def registered_counts(cls):
        return cls.cnt
    
    @property
    def color(self):
        return f"this is {self._color}"
    
    @color.setter
    def color(self, new_color: str):
        if str(new_color).isalpha():
            self._color = new_color
        else:
            print(f"{new_color} must be a color")
            
    @color.deleter
    def color(self):
        print(f"the color has been deleted")
        del self._color

    
    
    

class Circle(Shape):
    def __init__(self, color, isfill, radius):
        super().__init__(color, isfill)
        self.radius = radius
        
    def area(self):
        print(f"the area is {3.14 * self.radius ** 2}")
        
    def describe(self):
        print(f"this is {self._color} Circle, and it is {"filled" if self.isfill else "not filled"}")
        super().describe()
class Square(Shape):
    def __init__(self, color, isfill, width):
        super().__init__(color, isfill)
        self.width = width
    
    def area(self):
        print(f"the area is {self.width ** 2}")

    def describe(self):
        print(f"this is {self._color} Square, and it is {"filled" if self.isfill else "not filled"}")
        super().describe()
class Pizza(Circle):
    def __init__(self, color, isfill, radius, toping):
        super().__init__(color, isfill, radius)
        self.toping = toping
    
    
circle1 = Circle("red", True, radius=5)
circle2 = Circle("black", False, 8)
square1 = Square("black", False, width=5)

pizza1 = Pizza("yellow", True, 6, "cheeze")



# circle1.describe()
print(circle1.color)
circle1.color = 5

del circle1.color

