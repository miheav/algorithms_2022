"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import json
from hashlib import sha256

soil = '12345'

def generate_passwords():
    
    password = {'passwords': ['123', 'abv', '111']}
    hash = {'passwords':[], 'soil': soil}
    for i in password['passwords']:
        hash['passwords'].append(sha256(soil.encode('utf-8')+i.encode('utf-8')).hexdigest())
    
    with open('passwords.json', 'w') as outfile:
        outfile.write(json.dumps(hash))
    
    

    
#generate_passwords()



def get_password(password):
    passwords = {}
    with open('passwords.json') as json_file:
        passwords = json.load(json_file)

    hash = sha256(passwords['soil'].encode('utf-8')+password.encode('utf-8')).hexdigest()
    
    if hash in passwords['passwords']:
        return True 
    else:
        return False





password_1 = get_password(input("Введите пароль: "))

password_2 = input("Введите пароль еще раз: ")

if(password_1 and password_2):
    print("Вы авторизовались")
else:
    print("Введен неверный пароль")