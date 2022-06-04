"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
import collections
import functools
from collections import defaultdict
numbers = defaultdict(list)
# numbers[0] = list(input('Введите шестнадцатиричное число'))
# numbers[1] = list(input('Введите второе шестнадцатиричное число'))

numbers[0] = list('A2')
numbers[1] = list('C4F')
sum = list(hex(int(''.join(numbers[0]), 16) + int(''.join(numbers[1]), 16)))

print(f'sum = {sum}')


miltiply = list(hex(int(''.join(numbers[0]), 16) * int(''.join(numbers[1]), 16)))

print(f'miltiply = {miltiply}')

class Hex:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __add__(self, other):
        return list(hex(int(''.join(self.first), 16)
                        + int(''.join(other.second), 16)))

    def __mul__(self, other):

        return list(hex(int(''.join(self.first), 16)
                        * int(''.join(other.second), 16)))




sum = Hex(numbers[0], numbers[1]) +  Hex(numbers[0], numbers[1]) 
print(f'sum = {sum}')
miltiply = Hex(numbers[0], numbers[1]) *  Hex(numbers[0], numbers[1]) 
print(f'miltiply = {miltiply}')
