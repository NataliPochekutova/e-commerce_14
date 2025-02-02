# Приложение на основе e-commerce
## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/NataliPochekutova/e-commerce.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Основные модули, реализованные в проекте:
- Модуль utils.py. В нем реализованы функции, которые реализуют подгрузку данных по категориями и товарам из файла JSON
- Модуль product.py. В нем реализован класс, содержащий информацию о товарах
- Модуль category.py. В нем реализован класс, содержащий информацию об сатегориях товаров 
и списпи товаров из модуля product.py
- Модуль product_iterator.py. Класс, который производит итерацию по товарам
- Модуль new_product.py. В нем реализован классs-наследниками от исходного класса Product, 
содержащие категории "Smartphone" и "LawnGrass"

## Тестирование
Для проекта реализованы тесты на pytest. Запустить можно командой `pytest .`
Покрытие:
```
src\category.py                 32      0   100%
src\new_products.py             14      0   100%
src\product.py                  40      0   100%
src\product_iterator.py         14      0   100%
tests\conftest.py               41      0   100%
tests\test_category.py          31      0   100%
tests\test_new_products.py      17      0   100%
tests\test_product.py           56      0   100%
----------------------------------------------------------
TOTAL                          245      0   100%


```