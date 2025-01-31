class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        price = self.price * self.quantity
        return price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        '''
        name геттер
        '''
        return self.__name

    @name.setter
    def name(self, value: str):
        '''
        name сеттер
        value - новое имя, не длиннее 10 символов
        '''
        self.__name = value[:10]

    @classmethod
    def instantiate_from_cvs(cls):
        '''класс-метод, инициализирующий экземпляры класса
        "Item" данными из файла .../src/items.csv'''
        import csv
        import os
        cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for read in reader:
                cls(read['name'], read['price'], read['quantity'])

    @staticmethod
    def string_to_number(param):
        '''Метод, возвращающий число из числа-строки'''
        return int(float(param))





