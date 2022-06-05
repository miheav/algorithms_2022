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

Это файл для четвертого скрипта
"""
#python/Mikheev_Aleksey_dz_1/task_1_1.py /
from memory_profiler import profile

duration = [22, 60, 150, 4122, 40015, 150000]

@profile
def first():
    for data in duration:
        print("duration = " + str(data))
        if (data < 60):
            print (str(data) + " сек")
        elif (data < 60*60):
            minutes = data // 60
            seconds = data % 60
            print (str(minutes)+" мин " + str(seconds) + " сек")
        elif (data < 60*60*24):
            minutes = data // 60
            seconds = data % 60
            hours = minutes // 60
            minutes = minutes % 60
            print (str(hours) + " ч " + str(minutes)+" мин " + str(seconds) + " сек")
        else:
            minutes = data // 60
            seconds = data % 60
            hours = minutes // 60
            minutes = minutes % 60
            days = hours // 24
            hours = hours % 24
            print (str(days) + " д " + str(hours) + " ч " + str(minutes)+" мин " + str(seconds) + " сек")
        
@profile    
def second():
    for data in duration:
        print("duration = " + str(data))
        if (data < 60):
            print (f'{data} сек')
        elif (data < 60*60):
            minutes = data // 60
            seconds = data % 60
            print (f'{minutes}  {seconds} сек')
        elif (data < 60*60*24):
            minutes = data // 60
            seconds = data % 60
            hours = minutes // 60
            minutes = minutes % 60
            print (f'{hours} ч {minutes} {seconds} сек')
        else:
            minutes = data // 60
            seconds = data % 60
            hours = minutes // 60
            minutes = minutes % 60
            days = hours // 24
            hours = hours % 24
            print (f'{days} д {hours} ч {minutes} мин {seconds} сек')
            
            
first()
second()

# оптимизация разницы не выявила