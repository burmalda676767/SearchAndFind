class Shape:
    def init(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Метод area() має бути перевизначений у підкласі")

    def str(self):
        return f"{self.class.name}(color={self.color}, area={self.area():.2f})"


class Circle(Shape):
    def init(self, color, radius):
        super().init(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def init(self, color, width, height):
        super().init(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



circle = Circle(color="червоний", radius=5)
rectangle = Rectangle(color="синій", width=4, height=6)

print(circle)
print(rectangle)

print(f"Площа кола: {circle.area():.2f}")
print(f"Площа прямокутника: {rectangle.area():.2f}")