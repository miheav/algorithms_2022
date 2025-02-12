"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def func(var, e=0, o=0):
    
    

    """Рекурсия"""
    # все цифры числа извлечены
    if var == 0:
        return e, o
    else:
        # достаем очередную цифру числа
        cur_n = var % 10
        # число естественно становится короче
        var = var // 10
        # проверяем цифра четная или нечетная
        if cur_n % 2 == 0:
            e += 1
        else:
            o += 1
        return func(var, e, o)
    

print(func(int(input('Введите число: '))))