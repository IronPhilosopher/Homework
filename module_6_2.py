class Vehicle:
    __COLOR_VARIANTS = ["red", 'blue', 'yellow', 'brown', 'gray', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if str(new_color.casefold()) in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {str(new_color)}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedor', "Toyota Mark II", 'red', 500)

vehicle1.print_info()

vehicle1.set_color('magenta')
vehicle1.set_color('WHITE')
vehicle1.owner = "Alex"

vehicle1.print_info()
# Обращение через Vehicle.__COLOR_VARIANTS вызывает ошибку. С уважением, Тимур.
