"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit
import math 

def func(data):
    
    left_list = []
    right_list = []
    
    for i in range(len(data)):
        
        for b in range(len(data)):
            
            if data[i] > data[b]:
                left_list.append(data[b])
            elif data[i] < data[b]:
                right_list.append(data[b])
            elif data[i] == data[b] and i > b:
                left_list.append(data[b])
            else:
                right_list.append(data[b])
                
                
        if(len(left_list) == len(right_list)):
            return data[i]
                
    
    
m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]


print(func(orig_list[:]))


print(
    timeit(
        "func(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "func(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "func(orig_list[:])",
        globals=globals(),
        number=1000))


# Скрипт зависает