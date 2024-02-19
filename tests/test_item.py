import pytest
from src.item import Item, InstantiateCSVError

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

def test_unbroken_instantiate_from_csv():
    """Тестирование метода instantiate_from_csv в правильном состоянии."""
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 5

def test_broken_instantiate_from_csv():
    """Тестирование метода instantiate_from_csv в сломанном состоянии"""
    with pytest.raises(KeyError):
        Item.instantiate_from_csv('items.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items.csv')

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



"""Здесь надо написать тесты с использованием pytest для модуля item."""
