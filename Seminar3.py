import math


class Shape:
    def get_perimetr(self):
        pass

    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_perimetr(self):
        return 2*math.pi*self.r

    def get_area(self):
        return math.pi*self.r**2


circle1 = Circle(10)
print(circle1.get_perimetr())
print(circle1.get_area())


class Triangle (Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def get_perimetr(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimetr()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

triangle1 = Triangle (3, 4, 5)  
print(triangle1.get_perimetr())
print(triangle1.get_area())


# Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.

# Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# конструктор класса __init__ - метод инициализации класса Circle.
# get_area - метод для расчета площади круга
# get_perimeter - метод для расчета периметра окружности


# Контекст
# И наконец, последняя задача - по аналогии с кругом создать класс для треугольника и расчета его характеристик.

# Задача
# Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
# конструктор класса __init__ - метод инициализации класса.
# get_area - метод для расчета площади
# get_perimeter - метод для расчета периметра
