PI = 3.14
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        if isinstance(self, Cube):
            if len(sides) != 1:
                for i in range(self.sides_count):
                    self.__sides.append(1)
            else:
                for i in range(self.sides_count):
                    self.__sides.append(sides[0])
        else:
            if len(sides) != self.sides_count:
                for i in range(self.sides_count):
                    self.__sides.append(1)
            else:
                for i in sides:
                    self.__sides.append(i)
        self.__color = list(color)
        self.filled = False
    def get_color(self):
                return self.__color
    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *sides):
        check = True
        for i in sides:
            if not isinstance(i, int) or i <= 0:
                check = False
        if len(sides) == len(self.__sides) and check:
            return True
        else:
            return False
    def get_sides(self):
        return self.__sides
    def get_perimeter(self):
        return sum(self.__sides)
    def set_sides(self, *sides):
        if isinstance(self, Triangle):
            if self._Triangle__is_valid_triangle:
                self.__sides = list(sides)
        else:
            if self.__is_valid_sides(sides):
                self.__sides = list(sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / 2 / PI
    def get_square(self):
        return PI * self.__radius ** 2
    def __len__(self):
        return self.get_sides()[0]
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__is_valid_triangle()
    def __is_valid_triangle(self):  # Проверка неравенства треугольника
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        if a >= b + c or b >= a + c or c >= b + a:
            print('Треугольника с такими сторонами не существует, поэтому стороны вернулись к базовому значению')
            self.set_sides(1, 1, 1)
            return False
        else:
            return True
    def get_square(self):
        perimeter = self.get_perimeter()/2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return ((perimeter) * (perimeter - a) * (perimeter - b) * (perimeter - c)) ** 0.5
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle2 = Triangle([32, 45, 16], 1, 2, 3) # Невозможный треугольник
triangle1 = Triangle([6, 9, 8], 3, 4, 5) # Возможный треугольник

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# Проверка площади треугольника:
print(triangle1.get_square())