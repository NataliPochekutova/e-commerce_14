from src.category import Category
from src.product import Product
import pytest


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения доп. функций"
    assert len(category_1.products) == 95
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 13 шт"


def test_add_product(all_products):
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    all_products.add_product(product4)
    assert Category.product_count == 2


def test_add_product_smartphone(all_products, product_smartphone_1):
    product = product_smartphone_1
    all_products.add_product(product)
    assert Category.product_count == 2


def test_add_product_error():
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    category = Category("Смартфоны", "Смартфоны, как средство", [product4])
    with pytest.raises(TypeError):
        category.add_product(42)


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)
