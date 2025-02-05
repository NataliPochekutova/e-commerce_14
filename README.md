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
- Модуль order.py выводит информацию о том, какой товар был куплен, количество купленного товара, 
а также итоговая стоимость
- Модуль  print_mixin.py содержит класс-миксин, который печатает в консоль информацию о том, 
от какого класса и с какими параметрами был создан объект.
- Модули base_product.py и base_order.py содержат базовые абстрактные классы для Product и Category(Order)

## Тестирование
Для проекта реализованы тесты на pytest. Запустить можно командой `pytest .`
Покрытие:
```
src\base_order.py                5      1    80%   
src\base_product.py              6      1    83%   
src\category.py                 33      0   100%
src\new_products.py             14      0   100%
src\order.py                     9      0   100%
src\print_mixin.py               5      0   100%
src\product.py                  43      0   100%
src\product_iterator.py         14      0   100%
tests\conftest.py               41      0   100%
tests\test_category.py          31      0   100%
tests\test_new_products.py      17      0   100%
tests\test_order.py              5      0   100%
tests\test_print_mixin.py       12      0   100%
tests\test_product.py           56      0   100%
----------------------------------------------------------
TOTAL                          291      2    99%



```