import copy

# Базовий клас Prototype
class Shape:
    def clone(self):
        return copy.deepcopy(self)

# Конкретний клас – Коло
class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Circle(radius={self.radius}, color='{self.color}')"

# Конкретний клас – Прямокутник
class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color='{self.color}')"

# Демонстрація патерну Prototype
def main():
    # Створення оригінального об'єкта
    circle1 = Circle(5, "red")
    print("Original:", circle1)

    # Клонування об'єкта
    circle2 = circle1.clone()
    circle2.color = "blue"  # Зміна властивостей клона
    print("Clone:   ", circle2)

    # приклад з прямокутником
    rect1 = Rectangle(10, 20, "green")
    print("Original:", rect1)

    rect2 = rect1.clone()
    rect2.height = 30
    print("Clone:   ", rect2)

if __name__ == "__main__":
    main()