import pytest
from src.item import Item
from src.phone import Phone

data = Item("Смартфон", 10000, 20)
phone = Phone("iPhone 14", 120_000, 5, 2)


class Tests:
    def test__repr__(self):
        """Тест правильного вывода метода repr"""
        assert phone.__repr__() == f'Phone{"iPhone 14", 120_000, 5, 2}'

    def test__add__(self):
        """Тест правльиной работы метода add"""
        assert data.__add__(phone) == 25