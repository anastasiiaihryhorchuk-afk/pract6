class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

fig1 = Rectangle(20, 26)
fig2 = Rectangle(10, 13)

print(f"Перша фігура: {fig1.area()}")
print(f"Перша фігура: {fig1.perimeter()}")
print()
print(f"Друга фігура: {fig2.area()}")
print(f"Друга фігура: {fig2.perimeter()}")