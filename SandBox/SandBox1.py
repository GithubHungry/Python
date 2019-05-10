import sys
import os
import datetime
import time
import html
import random
import pprint  # Библиотека, которая выводит структуру данных в читаемом виде
import SearchFunctionForVowels

# print(sys.version) # Выводит варсию python (Библиотека sys)

# print(os.getcwd())  # Выводит имя папки в контексте которой выполняется код (Библиотека os)
# print(os.environ)  # Получаем доступ к системным переменным окружения всем сразу (Библиотека os)
# print(os.getenv('appdata'))  # Выводит конкретный атрибут функции environ (Библиотека os)

# print(datetime.date.today()) # Выводит текущую дату (Библиотека datetime)
# print(datetime.date.today().day)  # Выводит текущую дату[день] (Библиотека datetime)
# print(datetime.date.today().month)  # Выводит текущую дату[месяц] (Библиотека datetime)
# print(datetime.date.today().year)  # Выводит текущую дату[Год] (Библиотека datetime)
# print(datetime.date.isoformat(datetime.datetime.today()))# Вывод в формате YYYY-MM-DD [Текущая дата в виде строки?](Библиотека datetime)

# print(time.strftime("%I:%M"))  # Выводит текущее время [%I - в часах, %M - в минутах] в 12-часовом формате(Библиотека time)
# print(time.strftime("%a %p"))  # Выводит день недели и часть дня [%A - день недели %p - am или pm] (Библиотека time)

# print(html.escape("This HTML contains a &alt;script&gt;script&lt;/script&gt; tag."))  # Преобразование разметки в экранированный текст
# print(html.unescape("I &hearts; Pyt hon's &lt;standart library&gt;."))  # и обратно

# today = 'Saturday'  # Работа с циклом if-elif-else
# condition = 'normal'
# if today == 'Saturday':
#     if condition == 'Headache':
#         print('Not today:(')
#     else:
#         print('Party!')
# elif today == 'Sunday':
#     print('Recover.')
# else:
#     print('Work, work, work.')

# print(random.randint(1, 10))  # Печать случайного числа в диапазоне 1-10 (Библиотека Random)
# time.sleep(10)  # Задержка 10 секунд (Библиотека Time)
# print(random.randint(1, 10))

# print('Привет')  # Проверка русской кодировки

# hello = 'hello'  # Проба списков
# world = ['world']
# spis = [hello, world]
# print(spis)
# print(hello) # чтобы нормально было надо выводить через for-цикл
# sp = [[1, 2, 3], [1, 1, 1], ['a'], ['b'], ['c']]
# print(sp)

# volwes = ['a', 'o', 'i', 'e', 'u', 'y']  # Поиск гласных в слове (Капсом буквы не ищет)
# word = 'WallEy'
# for letter in word:
#     if letter in volwes:
#         print(letter)


# spis = ['a', 'b', 'c', 'd', 'e']
# print(spis)
# for num in spis:
# print(num)
# spis.remove('b')  # Принимает значение объекта в единственном аргументе
# spis.pop()  # Метод POP без параметра удаляет последний элемент в списке И ВОЗВРАЩАЕТ ЕГО
# k=spis.pop(3)  # Метод POP с параметром удаляет i-й элемент в списке И ВОЗВРАЩАЕТ ЕГО
# print(k)  # Сохранение возвращенного значения из метода POP в переменную
# spis.append(1)  # Добавление элемента в список (в конец), но НЕ возвращает его
# spis.extend([1, 2, 3])  # Добавление списка объектов в единственном аргументе (удобно для объединения двух списков)
# spisok = ['3', '2', '1']
# spis.insert(3, spisok)  # Добавление в нужную позицию
# new_spis = ''.join(spisok)  # Преобразовывет массив с троку (работатет только с символами, а не с числами)

# sp=[1,2,3,4]
# print(spis)
# spis.extend(sp)
# print(new_spis)
# print(spis)
# print(sp)
# spisochek = spis.copy()  # Копирует в переменную список
# sp.append(5)
# print (spis)
# print (sp)
# print(spisochek)

# print(spis[2])  # Вытягивает (возвращает) i-й элемент с начала
# print(spis[-2])  # Вытягивает (возвращает) i-й элемент с конца
# print(spis[0:4:1])  # Возвращает элементы начиная с i-го до j-того с шагом k
# print(spis[3:])  # Возвращает все элементы списка начиная с i-го
# print(spis[:4])  # Возвращает все элементы списка начиная с 0-го до i-го
# print(spis[::3])  # Возвращает все элементы списка начиная с 0-го до конца с шагом k

# book = "The Hitchhiker's Guide to the Galaxy"
# print(book)
# booklist = list(book)  # Преобразует строку в список
# print(booklist)
# print(booklist[:3])
# print(''.join(booklist[:3]))  # Возвращает преобразованный в строку список с 3-я первыми символами
# print(''.join(booklist[-6:]))  # Возвращает преобразованный в строку список с 6-ю последними символами
# print(''.join(booklist[::-1]))  # Возвращает преобразованный в строку список в обратном порядке
# print(''.join(booklist[::2]))  # Возвращает преобразованный в строку список с каждой второй буквой , начиная с 0
# print(''.join(booklist[4:16]))  # Возвращает определенный кусок из списка в виде строки (3 параметр опущен)
# print(''.join(booklist[15:3:-1]))  # Возвращает определенный кусок desc из списка в виде строки


# s1 = ['hello']  # Конкатенация
# s2 = [' ']
# s3 = ['world!']
# n_s1 = ''.join(s1)
# n_s2 = ''.join(s2)
# n_s3 = ''.join(s3)
# print(n_s1)
# print(n_s2)
# print(n_s3)
# print(n_s1 + n_s2 + n_s3)

# fruits = {}  # Создаем словарь
# fruits["apple"] = 10  # Добавляем в словарь элемент с ключом apple и значением 10
# fruits.setdefault('banana', 0)  # Setdefault гарантирует нам инициализацию несуществующих ключей(вместо 'banana')
# # может быть любое значение, в т.ч. и переменная (н-р в цикле for (см.Vowel set v_2.py))
# fruits['banana'] += 1  #
# print(fruits)

# letters = set('aaooeeiiuuyy')
# word = str(input("Введите строку:"))
# perem = letters.union(set(word))  # объединение множества и строки word переведенной в множество объектов-символов
# # PEREM - новое множество в котором объединены мн-во letters и переведенное в мн-во строка word
# print(word)
# print(letters)
# print(perem)
# sor_list = sorted(list(perem))  # Сортируем и преобразуем множество в список (БЕЗ ПОВТОРЕНИЙ)
# print(sor_list)
# diff = letters.difference(set(word))
# print(diff)

# list = ['a', 'o', 'e', 'i', 'u', 'y']
# print(type(list))  # Type() - Выведет тип объекта
# kort = ('a', 'o', 'e', 'u', 'y', 'i')  # Задание кортежа
# print(type(kort))
# list[0] = 'A'
# print(list)
# # kort[2]=5  # Ошибка , т.к. кортеж не может быть изменен
# # print(kort)  # Вывод ошибки :)

# Ne_kort = ('Python')  # ЭТО СТРОКА ,А НЕ КОРТЕЖ
# print(type(Ne_kort))
# kort = ('Python',)  # ЭТО КОРТЕЖ ИЗ 1 ЭЛЕМЕНТА
# print(type(kort))

# people = {}
# people['Ford'] = {'Name': 'Ford Perfect', 'Gender': 'Male', 'Occupation': 'Researcher',
#                   'Home Planet': 'Betelgeuse Seven'}
# people['Arthur'] = {'Name': 'Arthur Dent', 'Gender': 'Male', 'Occupation': 'Sandwich-Maker',
#                     'Home Planet': 'Earth'}
# people['Trillian'] = {'Name': 'Trillian McMillan', 'Gender': 'Female', 'Occupation': 'Mathematician',
#                       'Home Planet': 'Earth'}
# people['Robot'] = {'Name': 'Marvin', 'Gender': 'Unknown', 'Occupation': 'Paranoid Android',
#                    'Home Planet': 'Unknown'}
# pprint.pprint(people)  # Двойной вызов,т.к.мы в 2 слова импортили, а не в 4
# # for k, v in sorted(people.items()):  # founded.item() - возвращает список пар ключ/значение (ПРЕДПОЧТИТЕЛЬНЕЕ)
# #     # sorted(dictionary) - сортирует словарь (по ключам?)
# #     print(k, ',а детальнее:', v,)
# print(people['Arthur']['Occupation'])

# vowels = set('123456')
# print(vowels)

# print(SearchFunctionForVowels.binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(SearchFunctionForVowels.binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
# SearchFunctionForVowels.binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

# def change_r(arg: int):  # Аргумент передается по значению,т.е. не меняется
#     print('Before:', arg)
#     arg += 1
#     print('After:', arg)
#     return a
#
#
# def change_julia(arg: list):  # Аргумент передается по ссылке => меняется
#     print('before:', arg)
#     arg.append(666)
#     print('after', arg)
#
#
# list = [1, 2, 3, 4, 5]
# a = 1
# print(change_r(a))
# change_julia(list)
# print(a)
# print(list)

# todos = open('todos.txt', 'a')  # Открывает файл для записи в конец(а)
# print('Zapis1', file=todos)  # Запивывает в файл file=todos
# print('Zapis2', file=todos)
# print('Zapis3', file=todos)
# todos.close()  # Закрывает дескриптор
#
# tasks = open('todos.txt', 'r')  # Открывает файл для записи, по умолчании с параметром 'r'
# for string in tasks:
#     print(string, end='')  # end='' для убирания пробелов между строками вывода
# tasks.close()

with open('todos.txt') as fi:  # Конструкция with сама закрывает дескриптор файла
    for string in fi:
        print(string, end='')
