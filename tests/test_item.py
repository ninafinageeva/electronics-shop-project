import pytest
from src.item import Item

data = Item("Смартфон", 10000, 20)

@pytest.fixture()
def data():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(data):
    '''Проверяет правильность выполнения метода, который подситывает total price
    '''
    assert data.calculate_total_price() == 200000
    assert data.quantity == 20


def test_apply_discount(data):
    '''Проверяет правильность выполнения метода, который подситывает установленную скидку для конкретного товара
    '''
    data.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000.0

def test_name(data):
    """Тест сеттера сокращающего длину имени до 10(и) символов."""
    data.name = "Abrakadabra"
    assert len(data.name) == 10

def test_instantiate_from_csv():
    """
    Проверка метода инициализируеющнго экземпляры класса Item данными из файла src/items.csv
    """
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 5

def test_string_to_number(data):
    """
    Проверка метода преоброзвания строки в число
    """
    assert data.string_to_number("200") == 200

def test__repr__():
    """Тест правильного вывода информации для разработчика"""
    item1 = Item("Ноутбук", 50000, 2)
    assert repr(item1) == "Item('Ноутбук', 50000, 2)"
    assert str(item1) == 'Ноутбук'

def test__str__():
    """Тест правильного вывода информации для пользователя"""
    item1 = Item("Ноутбук", 50000, 2)
    assert str(item1) == 'Ноутбук'

def test__add__():
    """z"""
    item1 = Item("Ноутбук", 50000, 2)

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    test1 = Item.all[0]
    assert test1.name == "Смартфон"





"""Здесь надо написать тесты с использованием pytest для модуля item."""
