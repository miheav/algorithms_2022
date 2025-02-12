"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""






def first(list): #O(n^2)
    min = 999999999999999999999 #O(1)
    
    for j in list: 
        for b in list: #O(n^2)
            if j < b and j < min: #O(1)
                min = j #O(1)
                
    print("Минимальное число", min) #O(1)
                
            
def two(list): #O(n)
    min = 999999999999999999999 #O(1)

    for j in list: #O(n)
        if j < min: #O(1)
            min = j #O(1)
                
    print("Минимальное число", min) #O(1)           

#first([1,2,3,4,5,6,7,8,9,10,22,33,0,123,2334, -5])
two([1,2,3,4,5,6,7,8,9,10,22,33,0,123,2334, -5])
