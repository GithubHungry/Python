import sys
import os
import datetime
import time
import html
import random
import pprint  # Библиотека, которая выводит структуру данных в читаемом виде
import SearchFunctionForVowels
from threading import Thread
from datetime import datetime
import collections


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

# with open('todos.txt') as fi:  # Конструкция with сама закрывает дескриптор файла (Предпочтительнее)
#     for string in fi:
#         print(string, end='')

# names = ['Vadim', 'Oleg', 'Lisa', 'Nazar', 'Anton']
# print(names)
# perem = '|'.join(names)  # '|'.Join() Объединяет элементы списка в строку разделенную символом |
# print(perem)
# print(type(perem))
# per = perem.split('|')  # perem.split('|') преобразует строку в массив строк по разделителю |
# print(per)


# class CountFromBy:
#     pass
#
#
# obj1 = CountFromBy()
# obj2 = CountFromBy()

# def MyFunc(*args):  # Передаем любое кол-во аргументов (args просто заглушка, галвное *)
#     for a in args:  # Перебео каждого аргумента
#         print(a, end=' ')
#     if args:  # Вставляет пустую строку между вызовами
#         print()
#
#
# def MyFunc2(**kwargs):  # Передаем аргументы в словаре (именнованные аргументы)
#     for k, v in kwargs.items():  # key,values из словаря
#         print(k, v, sep='->', end=' ')  # Выбрать каждую пару ключ-значение из словаря и вывести на экран
#     if kwargs:
#         print()
#
#
# def MyFunc3(*args, **kwargs):  # Принимает Ваще любые параметры
#     if args:
#         for a in args:
#             print(a, end=' ')
#         print()
#     if kwargs:
#         for k, v in kwargs.items():
#             print(k, v, sep='->', end=' ')
#         print()
#
#
# sp = [1, 2, 3, 4, 5]
# MyFunc()
# MyFunc(10)
# MyFunc('a', 'b', 10)
# MyFunc(sp)  # Передаем список как 1 аргумент
# MyFunc(*sp)  # Передаем список как список аргументов(каждый элемент списка - это аргумент в функцию)
# MyFunc2(a=10, b=21)  # Вызов myfun2 (параметры задаются как k=а v=10)
# MyFunc3()
# MyFunc3(1, 2, 3)
# MyFunc3('xyz', a=100, b=500)

# try:
#     with open('myfile.txt') as fh:
#         file_data = fh.read()
#         print(file_data)
# # except FileNotFoundError:  # Обработка определенной ошибки
# #     print('The data file is missing!')
# except PermissionError:
#     print('Error?')
# # except:  # Обработка любых исключений
# #     print('Unknown error')
# except Exception as err:
#     print('Some other error occurred:', str(err))

# try:
#     1/0
# except:
#     err=sys.exc_info()
#     for e in err:
#         print(e)

# s = 'I DID NOT MEAN TO SHOUT'
# print(s)
# t = s.title()  # Преобразование букв верхнего регистр в слово с заглавной буквы
# print(t)
#
#
# def convert2ampm(time24: str) -> str:
#     return datetime.strptime(time24, '%H:%M').strftime("%I:%M%p")

# def factorial(n: int) -> int:  # recursion
#     """Find fact n"""
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))

# def greet(name: str) -> None:
#     print('hello' + name + '!')
#     greet2(name)
#     print('getting ready to say bye...')
#     bye()
#
#
# def greet2(name: str) -> None:
#     print('How are you ' + name + '?')
#
#
# def bye() -> None:
#     print('Bye-bye')
#
#
# greet('Vadim')


# print(20 // 3)  # Целочисленное деление
# print(20 ** 3)  # ** - степень
# print(20 % 3)  # Остаток от деления

# class Human:
#     name = 'Vadim'
#     age = 21
#
#     def __init__(self, name='vadim', age=21):  # А-ля конструктор
#         self.name = name
#         self.age = age
#
#     def set(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('Name is: ' + self.name)
#         print('Age is: ' + str(self.age))
#
#
# class Student(Human):
#     num = 620603
#
#     def __init__(self, num: int = 620603):
#         self.num = num
#
#     def set(self, name: str, age: int, num: int):
#         self.name = name
#         self.age = age
#         self.num = num
#
#     def show(self):
#         print(self.name + ' ' + str(self.age) + ' ' + str(self.num))
#
#
# man1 = Human()
# man1.set(name='Oleg', age=20)
# man1.show()
# print(man1.name + ' ' + str(man1.age))
# man2 = Human(name='anton', age=19)
# man2.show()
# man3 = Student(620601)
# man3.show()

# message = "Start learning python again..."
# print(message)
# message = "oh, fuck"
# print(message)

# name = 'ave maria!'
# print(name.title())
# print(name.upper())
# print(name.lower())
# first = 'ave'
# last = 'maria'
# latest = '!'
# full = first + " " + last + " " + latest
# print(full)

# message = "deus vult ! "
# print(message.strip())

# name = str(input("Enter your name : "))
# print("Hello "+name.title()+", would you like to learn some python today?")
# print(name.upper())
# print(name.lower())
# print(name.title())
# print('Albert Einstein once said , "A person who never made a mistake never tried anything new." ')
# print(name.title()+' once said , "A person who never made a mistake never tried anything new." ')

# names = ['Oleg', 'Egor', 'Nazar', 'Antony', 'Ellise']
# for name in range(len(names)):
#     print("Hi!" + names[name] + " is my friend.")
#
# brands = ['Bmw', 'Honda', 'Mercedes']
# print("I wanna "+brands[0].upper())
# print("I not wanna "+brands[1].upper())
# print("I wanna "+brands[2].upper())

# print(hex(21))

# guests = ['Oleg', 'Nazar', 'Antony']
# print(guests[0] + ",i wanna to invite you for lunch!")
# print(guests[1] + ",i wanna to invite you for lunch!")
# print(guests[2] + ",i wanna to invite you for lunch!")
# print("Shit," + guests[2] + " cant visit me")
# del guests[2]
# guests.append("Elisse")
# for guest in range(len(guests)):
#     print(guests[guest] + ",i wanna to invite you for lunch!")
# print("Ooo! Some new friends!")
# guests.insert(0, 'Egor')
# guests.insert(2,'Maks')
# guests.append('Miha')
# for guest in range(len(guests)):
#     print(guests[guest] + ",i wanna to invite you for lunch!")
# print("Pizda stoly!")
# print(guests.pop(1)+", sorry,but idi nahooy")
# print(guests.pop()+", sorry,but idi nahooy")
# print(guests.pop()+", sorry,but idi nahooy")
# print(guests.pop()+", sorry,but idi nahooy")
# for guest in range(len(guests)):
#     print(guests[guest] + ",i wanna to invite you for lunch!")
# del guests[1]
# del guests[0]
# print(guests)

# cars = ['bmw', 'audi', 'zapor', 'mercedes']
# print(cars)
# # print(sorted(cars, reverse=True))
# cars.reverse()
# print(cars)

# countries = ['France', 'America', 'China', 'England', 'Sydney']
# for country in countries:
#     print(country )
# print(countries)
# print(sorted(countries))
# print(countries)
# print(sorted(countries, reverse=True))
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
# print(len(countries))

# pizzas = ['pepperoni', 'bbq', 'chesse']
# for pizza in pizzas:
#     print("I like "+pizza+" pizza!")
# print("i really like pizza!")

# for num in range(1, 11):
#     print(num ** 2)
#
# squares = []
# for num in range(1, 11):
#     squares.append(num ** 2)
# print(squares)

# list = [value ** 3 for value in range(1, 11)]
# print(list)
# chisla = [value for value in range(3, 31,3)]
# print(sum(chisla))
# for chislo in chisla:
#     print(chislo)
# print(chisla)

# cars = ['bmw', 'audi', 'mercedes', 'zapor', 'lada']
# print('The first three items in the list are: ')
# for car in cars[:3]:
#     print(car.title())
# print('The middle three items in the list are: ')
# for car in cars[1:4]:
#     print(car.title())
# print('The last three items in the list are: ')
# for car in cars[-3:]:
#     print(car.title())

# pizzas = ['pepperoni', 'bbq', 'chesse']
# new_pizzas = pizzas.copy()
# print(pizzas)
# print(new_pizzas)
# pizzas.append('margaret')
# new_pizzas.append('mushrooms')
# print("Old pizzas are :")
# for pizza in pizzas:
#     print(pizza)
# print("New pizzas are :")
# for n_pizza in new_pizzas:
#     print(n_pizza)

# rectangle = (200, 500)
# print(rectangle)

# menu = ('rice', 'potato', 'meat', 'fish', 'bread')
# for dish in menu:
#     print(dish.title())
# menu = ('vodka', 'beer', 'coctail')
# for dish in menu:
#     print(dish.title())

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'Subaru'
# print(car == 'Subaru')
# print("is it car == 'subaru'?, i think true")

# alien_color = 'red'
# if alien_color == 'green':
#     print("5 points")
# elif alien_color == 'yellow':
#     print("10 points")
# else:
#     print("100 points")

# users = ['Oleg', 'Nazar', 'Liza', 'Anton', 'Admin']
# if users:
#     for user in users:
#         if user == 'Admin':
#             print("Hello, admin, would you like to see a status report?")
#         else:
#             print("Hello, " + user + ", thank you for logging in again")
# else:
#     print("We need to find some users")

# current_users = ['Oleg', 'Nazar', 'Liza', 'Anton', 'Admin']
# new_users = ['Nazar', 'Vadim', 'Egor', 'Igor', 'Alex', 'LIZA']
# spis = []
# for i in new_users:
#     for j in current_users:
#         if i.lower() == j.lower():
#             print('Error ' + i)
#             spis.append(i)
#     if i not in spis:
#         print("Hello, "+i)

# numbers = [val for val in range(1, 11)]
# for num in numbers:
#     if num == 1:
#         print(str(num)+'st')
#     elif num == 2:
#         print(str(num)+'nd')
#     elif num == 3:
#         print(str(num)+'rd')
#     else:
#         print(str(num)+'th')

# friends = ['Oleg', 'Nazar']
# langs = {'Vadim': 'Python', 'Oleg': 'JS', 'Liza': 'C#', 'Nazar': 'Ruby', 'Anton': 'C#'}
# for man, lang in langs.items():
#     print(man.upper() + "'s favorite language is " + lang)
# for name in langs:
#     print(name)
# for name in langs.keys():
#     if name in friends:
#         print('Hello, ' + name + ', your favoirite language is:' + langs[name])
# if 'Bill' not in langs.keys():
#     print('Bill take our pool!')

# slovoSPB = {'MC': 'Oxxxymiron', 'Sonya': 'Marmeladova', 'Vitya': 'ST'}
# for key, value in slovoSPB.items():
#     print('key: ' + key)
#     print('value: ' + value)

# man = {'first_name': 'Bardier', 'last_name': 'Vadim', 'age': '21', 'city': 'Minsk'}
# print(man['first_name'])
# print(man['last_name'])
# print(man['age'])
# print(man['city'])
# for key, val in man.items():
#     print(key, val)

# langs = {'Vadim': 'Python', 'Oleg': 'JS', 'Liza': 'C#', 'Nazar': 'Ruby', 'Anton': 'C#'}
# for name, language in sorted(langs.items()):
#     print(name + " " + language)
# for language in sorted(set(langs.values())):
#     print(language)

# rivers = {'nile': 'Egypt', 'amazonka': 'USA', 'volga': 'Russia'}
# for name, country in rivers.items():
#     print(name + ' ' + country)
# for name in sorted(rivers.keys()):
#     print(name)
# for country in sorted(rivers.values()):
#     print(country)

# langs = {'Vadim': 'Python', 'Oleg': 'JS', 'Liza': 'C#', 'Nazar': 'Ruby', 'Anton': 'C#'}
# must_have = ['nazar', 'liza', 'egor']
# for must in must_have:
#     if must.title() in langs.keys():
#         print(must.title() + ' thanks')
#     else:
#         print(must.title() + ' please take part in a pool')

# alien_0 = {'color': 'red', 'points': '15'}
# alien_1 = {'color': 'yellow', 'points': '10'}
# alien_2 = {'color': 'green', 'points': '5'}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'speed': 'high', 'color': 'red', 'points': '15'}
#     aliens.append(new_alien)
# print("kol-vo: " + str(len(aliens)))
#
# for alien in aliens[:3]:
#     if alien['color'] == 'red':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in aliens[:5]:
#     print(alien)

# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
# print("Your order is: " + pizza['crust'] + " - type of crust, pizza toppings: ")
# for topping in pizza['toppings']:
#     print(topping)

# pool = {'Vadim': ['Python', 'PHP'], 'Oleg': ['JS', 'HTML'], 'Liza': ['C#']}
# for name, lang in pool.items():
#     if len(lang) == 1:
#         print(name + "'s favorite language is: " )
#         for language in pool[name]:
#             print(language)
#     else:
#         print("Name: " + name + ", favorite languages: ")
#         for lang in pool[name]:
#             print(lang)

# users = {'aeinstein': {'first': 'Albert', 'last': 'Einstein', 'location': 'Minsk'},
#          'mcurie': {'first': 'Maria', 'last': 'Curie', 'location': 'Paris'}}
# for user_name, user_info in users.items():
#     print("User name is: " + user_name)
#     full_name = user_info['first'] + " " + user_info['last']
#     print("Full name is: " + full_name + ", location:" + user_info['location'])
#     # for key, val in users.items():
#     #     print(key + ": " + str(val))

# Vadim = {'first': 'Vadim', 'last': 'Bardier', 'city': 'Minsk'}
# Oleg = {'first': 'Oleg', 'last': 'Cuprianov', 'city': 'Vitebsk'}
# Arina = {'first': 'Arina', 'last': 'Goncharova', 'city': 'Brest'}
# people = [Vadim, Oleg, Arina]
# for p in people:
#     for k, v in p.items():
#         print(k + ": " + v)

# jojo = {'name': 'Jorjik', 'owner': 'Vadim'}
# mart = {'name': 'Martin', 'owner': 'Liza'}
# pets = [jojo, mart]
# for pet in pets:
#     for k, v in pet.items():
#         print(k + ": " + v)
#     print("New pet...")

# favorite_places = {'pyramids': ["Liza", "Antony"], "effel tover": ["Antony", "Vadim"], "white house": ["Nazar",
# "Liza"]}
# for k, v in favorite_places.items():
#     print("new place is:")
#     print(k + " is favorite place for: ")
#     for person in v:
#         print(person)

# cities = {'Minsk': {'country': 'Belarus', 'population': 10}, 'Paris': {'country': 'France', 'population': 25},
#           'Moscow': {'country': 'Russia', 'population': 100}}
# for k, v in cities.items():
#     print(k + ": ")
#     for info in v.values():
#         print(info)

# # Транспонирование матрицы
# matrix = [[0.5, 0, 0, 0, 0],
#           [1, 0.5, 0, 0, 0],
#           [1, 1, 0.5, 0, 0],
#           [1, 1, 1, 0.5, 0],
#           [1, 1, 1, 1, 0.5]]
#
# matrix_t = list(zip(*matrix))  # Транспонирование
# # аналог(matrix[0], matrix[1], matrix[2], matrix[3])
#
# for element in matrix:
#     print(element)
# print('*' * 17)
# for element in matrix_t:
#     print(element)
#
# # Транспонирование ч2
# days = ('пн', 'вт', 'ср', 'чт')
# energy_1 = (1584.5, 596.5, 2417.6, 3695.5)
# energy_2 = (6587.2, 148.3, 6547.2, 2473.2)
# args = (days, energy_1, energy_2)
# # ('пн',1584.5,6587.2)
# result = list(zip(*args))  # первая, вторая, третья, четвертая строка
# # посмотреть про аргументы и их количество
# print(result)

# hello_message = 'Print me something and i repeat all'
# hello_message += '\n\tType "quit" to end the program: '
# # message = ' '  # must have,т.к. если нет данных для сравнения, то работа дальше не возможна
# active = True
# while active:
#     message = input(hello_message)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# enter_message = "Please, enter the name of a city"
# enter_message += "\n\t type 'quit' to end the program"
# while True:
#     message = input(enter_message)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# hello_message = 'Please, type name of topping, which you want to add:'
# hello_message += '\nType quit to end :'
# active = True
# while active:
#     topping = input(hello_message)
#     if topping != 'quit':
#         print("You add " + topping + " in your order")
#     else:
#         active = False

# hello_message = "Please, enter your age: "
# while True:
#     age = input(hello_message)
#     if age.isdigit():
#         age = int(age)
#         if (age >= 3) and (age <= 12):
#             print("10$")
#             break
#         elif age > 12:
#             print("15$")
#             break
#         elif age < 3:
#             print("It`s free for you.")
#             break
#     elif age == 'exit':
#         print("Bye, see you next time")
#         break
#     else:
#         print('error')
#         continue

# unverified_users = ['Oleg', 'Vadim', 'Nazar']
# verified_users = []
# while unverified_users:
#     current_user = unverified_users.pop()
#     print("Verifying... Complete! User " + current_user + " successfully verified!")
#     verified_users.append(current_user)
#     print('*'*55)
# print("Verified users: ")
# for user in verified_users:
#     print(user)

# pool = {}
# flag = True
# while flag:
#     name = input('Please, enter your name: ')
#     answer = input('Please, enter your favorite number: ')
#     pool[name] = answer
#     cont = input('Continue ? (y/n) ')
#     if cont == 'n':
#         print('Bye!')
#         flag = False
#     elif cont == 'y':
#         continue
#     else:
#         print('Incorrect letter.Bye :|')
#         flag = False
# for k, v in pool.items():
#     print(k + " : " + v)

# order_sandwiches = ['sw_1', 'sw_2', 'sw_3', 'sw_1', 'sw_4', 'sw_1']
# finished_sandwiches = []
# print("Warning, there is no sw_1 in our coffee!")
# while 'sw_1' in order_sandwiches:
#     order_sandwiches.remove('sw_1')
# while order_sandwiches:
#     current_sw = order_sandwiches.pop()
#     print("Now, I cook " + current_sw + "!")
#     finished_sandwiches.append(current_sw)
# for sw in finished_sandwiches:
#     print(sw)

# def greet_users():
#     """Simple hello @all"""
#     print('Hello, traveller!')
#
#
# def greet_users_name(user_name: str):
#     """Simple hello @user_name"""
#     print('Hello, traveller (' + user_name.title() + ")!")
#
#
# greet_users()
# greet_users_name('Vadim')

# def display_message(message: str):
#     print("Theme: " + message)
#
#
# display_message('Functions')

# def animal_info(animal_type: str, animal_name: str):
#     """Print info about animal"""
#     print("I have " + animal_type.lower())
#     print("My " + animal_type.lower() + "`s name is " + animal_name.title())
#
#
# animal_info('humster', 'homa')


# def make_shirt(text: str, size='L'):
#     print("Size: " + size + ", text: " + text)
#
#
# make_shirt('You suck')
# make_shirt(text='OOOoaAAA', size='M')

# def fully_name(first_name: str, last_name: str, age=''):
#     """ men`s info """
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# men = fully_name('Vadim', 'Bardier', 21)
# print(men)

# def city_country(city_name: str, country_name):
#     full = city_name + ', ' + country_name
#     return full
#
#
# one = city_country("Minsk", "Belarus")
# two = city_country("Moscow", "Russia")
# three = city_country("Paris", "France")
# print(one)
# print(two)
# print(three)

# def song_album(song_name: str, album_name: str, number='') -> dict:
#     """return song+album(+number of songs in album"""
#     song_alb = {"song": song_name, "album": album_name}
#     if number:
#         song_alb['number'] = number
#     return song_alb
#
#
# one = song_album("Minsk", "Belarus")
# two = song_album("Moscow", "Russia", 21)
# three = song_album("Paris", "France", 3)
# print(one)
# print(two)
# print(three)
# while True:
#     song_name = input("Please, enter song name: ")
#     if song_name == 'q':
#         break
#     album_name = input("Please, enter album name: ")
#     if album_name == 'q':
#         break
#     number = input("Please, enter number of songs in album: ")
#     if number == 'q':
#         break
#     temp = song_album(song_name, album_name, number)
#     print(temp)

# def greetings(names: list):
#     for name in names:
#         print("Greetings, " + name.title())
#
#
# names_users = ['vadim', 'oleg', 'egor']
# greetings(names_users)

# def printer_fun(order):
#     finished = []
#     while order:
#         finished.append(order.pop())
#     return finished
#
# order = ['d1', 'd2', 'd3']
# print(printer_fun(order))
# print(order)

# def show_magicians(names: list):
#     for name in names:
#         print(name.title())
#
#
# def make_great(names: list):
#     for i in range(len(names)):
#         names[i] = "Great " + names[i]
#
#
# names = ['vadim', 'egor', 'oleg']
# make_great(names)
# show_magicians(names)

# def make_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
#
#
# make_pizza('peperoni')
# make_pizza('mushrooms', 'extra cheese', 'more meat')
# make_pizza()

# def built_info(first_name, last_name, **add_info):
#     """Return dict with info about people"""
#     person = {}
#     person['first_name'] = first_name
#     person['last_name'] = last_name
#     for k, v in add_info.items():
#         person[k] = v
#     return person
#
#
# person1 = built_info('Vadim', 'Bardier', status='student', location='Minsk')
# print(person1)

# def make_sw(*args) -> None:
#     print("Your sw consists of: ")
#     for part in args:
#         print('-' + part)
#
#
# make_sw()
# make_sw('bread', 'cheese', 'tomato')
# make_sw('bread', 'meat')

# def built_profile(first, last, **args):
#     profile['first_name'] = first
#     profile = {}
#     profile['last_name'] = last
#     for k, v in args.items():
#         profile[k] = v
#     return profile
#
#
# print(built_profile('vadim', 'bardier', age=21))


# class Dog():
#     """Класс создающий собаку"""
#
#     def __init__(self, name, age):
#         """Иницифлизация атрибутов собаки"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Собака садится по команде"""
#         print(self.name.title() + " is sitting now.")
#
#     def roll_over(self):
#         """Собака перекатывается по команде"""
#         print(self.name.title() + " rolled over.")
#
#
# my_dog = Dog('Jojo', 8)
# print("My dog`s name is: "+my_dog.name.title()+'.')
# print("He is "+str(my_dog.age)+"-years old.")
# my_dog.sit()
# my_dog.roll_over()
#
# any_dog = Dog('Luci', 3)
# print("Any dog`s name is: "+any_dog.name.title()+'.')
# print("She is "+str(any_dog.age)+"-years old.")
# any_dog.sit()
# any_dog.roll_over()

# class Restaurant():
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#
#     def show_info(self):
#         """Show information about restaurant"""
#         print("This is a great restaurant : " + self.name.title() + " with " + self.cuisine + " cuisine.")
#
#     def work_time(self):
#         """Print restaurant work time"""
#         print(self.name.title() + " is work in format: 24/7")
#
#
# amster = Restaurant('amsterdam', 'europe')
# print("Name: " + amster.name + ", cuisine: " + amster.cuisine + ".")
# amster.show_info()
# amster.work_time()

# class User():
#     def __init__(self, first_name, last_name, **info):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.info = {}
#         for k, v in info.items():
#             self.info[k] = v
#
#     def describe_user(self):
#         """Describe current user"""
#         full_name = self.first_name.title() + ' ' + self.last_name.title()
#         print("User: " + full_name + ", additional information: ")
#         if not self.info:
#             print('No info')
#         else:
#             for k, v in self.info.items():
#                 print("- " + k.title() + ": " + v.title())
#         print("")
#
#     def greetings(self):
#         """Приветствует пользователя"""
#         print("Greetings, " + self.first_name + " " + self.last_name + " !")
#
#
# class Privileges():
#     def __init__(self, *privileges):
#         self.privileges = []
#         for priv in privileges:
#             self.privileges.append(priv)
#
#     def show_privileges(self):
#         print("This user has privileges: ")
#         for privelegue in self.privileges:
#             print("- " + privelegue)
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()
#
#
# au1 = Admin('Vadim', 'Bardier')
# au1.privileges.privileges = ['fuck you', 'del you', 'edit you']
# au1.greetings()
# au1.describe_user()
# au1.privileges.show_privileges()
# u1 = User('vadim', 'bardier', location='Minsk')
# u2 = User('oleg', 'cuprianov', location='Vitebsk')
# u3 = User('egor', 'garbuz')
# u4 = User('liza', 'novik', location='Mosty')
# u1.greetings()
# u2.greetings()
# u3.greetings()
# u4.greetings()
# u1.describe_user()
# u2.describe_user()
# u3.describe_user()
# u4.describe_user()

# class Car():
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.odometr = 0
#
#     def description(self):
#         """return full description in normal type"""
#         full_desc = self.brand + ", " + self.model + ", " + str(self.year)
#         return full_desc
#
#     def show_odo(self):
#         print("This car has " + str(self.odometr) + " miles on it.")
#
#     def update_odometr(self, new_val):
#         self.odometr = new_val
#
#     def increment_odo(self, incr):
#         self.odometr += incr
#
#
# class Battery():
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def cap_of_battery(self, size):
#         self.battery_size = size
#
#     def get_range(self):
#         if self.battery_size < 70:
#             range = 240
#         else:
#             range = 270
#         message = "This car can gp approximately less than " + str(range) + " miles on a full charge"
#         print(message)
#
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)
#         self.battery = Battery()


# c1 = Car('BMW', 'x6', 2018)
# print(c1.description())
# c1.show_odo()
# c1.update_odometr(21)
# c1.show_odo()
# c1.increment_odo(5)
# c1.show_odo()
# c2 = ElectricCar('Tesla', 'model s', 2016)
# print(c2.description())
# c2.show_odo()
# my_tesla = ElectricCar('Tesla', 'model s', 2020)
# print(my_tesla.description())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.cap_of_battery(50)
# my_tesla.battery.battery_size = 21
# my_tesla.battery.describe_battery()

# class Restaurant():
#     def __init__(self, name, cuisine='none'):
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 0
#
#     def show_info(self):
#         """Show information about restaurant"""
#         print("This is a great restaurant : " + self.name.title() + " with " + self.cuisine + " cuisine.")
#
#     def work_time(self):
#         """Print restaurant work time"""
#         print(self.name.title() + " is work in format: 24/7")
#
#     def update_serv(self, new_val):
#         """update atr mu,ber_served"""
#         self.number_served = new_val
#
#     def increment_serv(self, incr_val):
#         """Increment number_served"""
#         self.number_served += incr_val
#
#     def show_num(self):
#         """Show num_served value"""
#         print(self.number_served)
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, name, *flavors):
#         super().__init__(name)
#         self.flavors = []
#         for flavor in flavors:
#             self.flavors.append(flavor)
#
#     def describe_stand(self):
#         print("This stand: " + self.name + " has the following IceCreams:")
#         for flavor in self.flavors:
#             print("- " + flavor)


# amster = Restaurant('amsterdam', 'europe')
# print("Name: " + amster.name + ", cuisine: " + amster.cuisine + ".")
# amster.show_info()
# amster.work_time()
# print(amster.number_served)
# amster.update_serv(21)
# amster.show_num()
# amster.number_served = 300
# amster.show_num()
# amster.increment_serv(1000)
# amster.show_num()
# pinguins = IceCreamStand('33-pinguins', 'strawberry', 'apple', 'orange')
# print(pinguins)
# pinguins.describe_stand()

# from collections import OrderedDict
#
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
# for k, v in favorite_languages.items():
#     print(k + ": " + v)

# from random import randint
#
#
# class Die():
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def input_sides(self):
#         self.sides = int(input("Enter number of sides: "))
#         print("Now you figure has " + str(self.sides) + " sides.")
#
#     def roll_die(self):
#         x = randint(1, self.sides)
#         return x
#
#
# figure = Die()
# for i in range(10):
#     print(figure.roll_die())
# six.input_sides()
# print(six.roll_die())

# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can`t divide by zero!")

# while True:
#     first_num = input('Enter first number: ')
#     if first_num == 'q':
#         break
#     second_num = input('Enter second number: ')
#     if second_num == 'q':
#         break
#     try:
#         print(int(first_num) / int(second_num))
#     except ZeroDivisionError:
#         print('Ты че, дебил?')
#         break

# q = collections.deque()
# q.append(21)
# q.appendleft(25)
# q.appendleft(31)
# print(q)
# x = q.popleft()
# print(x)
# x = q.pop()
# print(x)
# for el in q:
#     print(el)
# print(q)

def qsort(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort([x for x in list[1:] if x < pivot])
        greater = qsort([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater


list1 = [1,1]
list = [0, 0, 0, 1, 2, 3, 4, 10, 21, 21, 0, 5, 6]
print(qsort(list1))
