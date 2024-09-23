class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = [sides]
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
        else:
            print("Invalid color")

    def __is_valid_sides(self, *sides):
        if self.sides_count == len(sides):

            for i in sides:
                if type(i) == int and i > 0:
                    continue
                else:
                    return False
            return True

        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        per = 0
        for i in self.__sides:
            per += i
        return per

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Invalid sides')

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = len(self)/6.28
        if len(self.get_sides()) != self.sides_count:
            self.set_sides = (1)

    def get_square(self):
        return (self.__radius*3.14)**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides = (1, 1, 1)

    def get_square(self):
        hp = len(self)//2
        a = self.get_sides([0])
        b = self.get_sides([1])
        c = self.get_sides([2])
        return round((hp*(hp-a)*(hp-b)*(hp-c))**0.5)

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        cs = []
        if len(self.get_sides()) != 1:
            for i in range(12):
                cs.append(1)
            self.set_sides(*cs)
        else:
            for i in range(12):
                cs.append(sides)
            self.set_sides(*cs)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

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
