"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""
#python/Mikheev_Aleksey_dz_9/task_9_2.py 

from pympler import asizeof

class Road:

    weight_1sm = 25
    sm = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):

        return self._length * self._width * self.weight_1sm * self.sm

    
asd = Road(5, 2)
print(asd.calculation())
print(asizeof.asizeof((asd))) 
class RoadNew:
    __slots__ = ['_length', '_width', 'weight_1sm', 'sm']


    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight_1sm = 25
        self.sm = 5
        
    def calculation(self):

        return self._length * self._width * self.weight_1sm * self.sm
    
    
asd = RoadNew(5, 2)
print(asd.calculation())
print(asizeof.asizeof((asd))) 


# 1250
# 328
# 1250
# 160
# Потребление памяти уменьшилось вдвое