"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit


lst = [i for i in range(10 ** 7)]


deq = deque([i for i in range(10 ** 7)])


def append_list():
    for i in range(0, 10 ** 4):
        lst.append(i)


# append
def append_deque():
    for i in range(0, 10 ** 4):
        deq.append(i)

# print(timeit('append_list()', globals=globals(), number=1000))
# print(timeit('append_deque()', globals=globals(), number=1000))
# 0.5916477999999188
# 0.43774060000214376

def pop_list():
    for i in range(0, 10 ** 4):
        lst.pop()


# append
def pop_deque():
    for i in range(0, 10 ** 4):
        deq.pop()

# print(timeit('pop_list()', globals=globals(), number=1000))
# print(timeit('pop_deque()', globals=globals(), number=1000))

# 0.3651811000017915
# 0.3594450999989931




def extend_list():
    for i in range(0, 10 ** 4):
        lst.extend(['a',1,2])


# append
def extend_deque():
    for i in range(0, 10 ** 4):
        deq.pop()
        
        
# print(timeit('extend_list()', globals=globals(), number=1000))
# print(timeit('extend_deque()', globals=globals(), number=1000))

# 1.3808323000012024
# 0.3784793999984686




def appendleft_list():
    for i in range(0, 10):
        lst.insert(0, i)




def appendleft_deque():
    for i in range(0, 10):
        deq.appendleft(i)



# print(timeit('appendleft_list()', globals=globals(), number=100))
# print(timeit('appendleft_deque()', globals=globals(), number=100))
# 8.27942670000266
# 0.0018506000014895108

# pop
def popleft_list():
    for i in range(0, 10):
        lst.pop(i)



# popleft
def popleft_deque():
    for i in range(0, 10):
        deq.popleft()



# print(timeit('popleft_list()', globals=globals(), number=100))
# print(timeit('popleft_deque()', globals=globals(), number=100))
# 6.709586000000854
# 4.990000161342323e-05


# insert
def extendleft_list():
    for i in range(0, 10):
        lst.insert(0, ['a',1,2])



# extend
def extendleft_deque():
    for i in range(0, 10):
        deq.extendleft(['a',1,2])



print(timeit('extendleft_list()', globals=globals(), number=100))
print(timeit('extendleft_deque()', globals=globals(), number=100))
# 8.36115769999742
# 0.00013279999984661117



#Дек быстрее во всем