"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from timeit import timeit
from collections import OrderedDict

dict = {}  # обычный словарь
order_dict = OrderedDict()  # OrderedDict
n = 10 ** 5  # число операций


def append_dict():
    for i in range(n):
        dict[i] = i
    
    
def append_order_dict():
    for i in range(n):
        order_dict[i] = i
        
        
append_dict()
append_order_dict()

# print(timeit('append_dict()', globals=globals(), number=100))
# print(timeit('append_order_dict()', globals=globals(), number=100))
# 0.41077059999952326
# 0.562902400000894


def append_dict(dict):
    for i in range(n):
        dict.popitem()
    
    
def append_order_dict(order_dict):
    for i in range(n):
        order_dict.popitem()
        
        
print(timeit('append_dict(dict.copy())', globals=globals(), number=100))
print(timeit('append_order_dict(order_dict.copy())', globals=globals(), number=100))
# 0.6028045999992173
# 1.7452252000002773


# Обычный словарь работает быстрее, упорядоченный словарь можно использовать если необходимы специфичные для его использования функции