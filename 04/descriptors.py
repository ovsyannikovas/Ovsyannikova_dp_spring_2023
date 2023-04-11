class Integer:
    def __init__(self):
        self.__value = None

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.__value = value
        else:
            raise Exception('Недопустимое значение для целого числа.')

    def __get__(self, instance, owner):
        return self.__value


class String:
    def __init__(self):
        self.__value = None

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.__value = value
        else:
            raise Exception('Недопустимое значение для строки.')

    def __get__(self, instance, owner):
        return self.__value


class PositiveInteger:
    def __init__(self):
        self.__value = None

    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            self.__value = value
        else:
            raise Exception('Недопустимое значение для положительного числа.')

    def __get__(self, instance, owner):
        return self.__value


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price
