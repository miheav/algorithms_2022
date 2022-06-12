"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
import statistics
from random import randint
from timeit import timeit

orig_list = [randint(0, 1000) for _ in range(10)]

print(orig_list)
print(statistics.median(orig_list[:]))


print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))


# 

# 0.000422299955971539
# 0.0023975999793037772
# 0.035251300025265664

# По результатам тестирования нахожнеие медианной было самым быстрым с использованием встроенной фукцнии


