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

# favorite_places = {'pyramids': ["Liza", "Antony"], "effel tover": ["Antony", "Vadim"], "white house": ["Nazar", "Liza"]}
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
