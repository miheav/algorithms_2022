"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from time import time


def decorator(function):

   def wrapper(*args, **kwargs):
      start = time()
      function(*args, **kwargs) # Сама функция
      end = time()
      print(f'Время выполенения функции {function.__name__} '
              f'составило {end - start}')

   return wrapper
 
list = []
@decorator
def list_fill(i):
   
   for i in range(0, i): #O(n)
      list.append(i)
   
   
dict = {}   
@decorator
def dict_fill(i):
   for i in range(0, i): #O(n)
      dict[i] = i
      
      


@decorator
def list_get(i):
   return list[i] #O(1)

@decorator
def dict_get(i):
   return dict[i] #O(1)




@decorator
def list_del(i):
   list.remove(i) #O(1)

@decorator
def dict_del(i):
  del dict[i] #O(1)
  
  
  
list_fill(10 ^ 10000000)
dict_fill(10 ^ 10000000)
# Список заполняется быстрее потому его структура проще


list_get(50041)
dict_get(50041)
# получение элемента одинакого
  
list_del(50041)
dict_del(50041)
# удаление списка медленннее