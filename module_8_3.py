class Car:

    def __init__(self, model: str, vin, numbers):
        self.model = model
        self.__is_valid_vin(vin)
        self.__vin = vin
        self.__is_valid_numbers(numbers)
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        else:
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber("Неверный диапазон для vin номера")
            else:
                return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber("Некорректный тип данных для номеров")
        else:
            if not len(numbers) == 6:
                raise IncorrectCarNumber("Неверная длина номера")
            else:
                return True
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')