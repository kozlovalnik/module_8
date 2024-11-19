class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vit = vin
        self.__numbers = numbers
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            pass

    def __is_valid_vin(self, vin_number: int) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
