import sys
import os
import datetime
import time
import html

# print(sys.version) # Выводит варсию python (Библиотека sys)

# print(os.getcwd())  # Выводит имя папки в контексте которой выполняется код (Библиотека os)
# print(os.environ)  # Получаем доступ к системным переменным окружения всем сразу (Библиотека os)
# print(os.getenv('appdata'))  # Выводит конкретный атрибут функции environ (Библиотека os)

# print(datetime.date.today()) # Выводит текущую дату (Библиотека datetime)
# print(datetime.date.today().day)  # Выводит текущую дату[день] (Библиотека datetime)
# print(datetime.date.today().month)  # Выводит текущую дату[месяц] (Библиотека datetime)
# print(datetime.date.today().year)  # Выводит текущую дату[Год] (Библиотека datetime)
# print(datetime.date.isoformat(datetime.datetime.today()))# Вывод в формате YYYY-MM-DD [Текущая дата в виде строки?](Библиотека datetime)

#print(time.strftime("%I:%M"))  # Выводит текущее время [%I - в часах, %M - в минутах] в 12-часовом формате(Библиотека time)
#print(time.strftime("%a %p"))  # Выводит день недели и часть дня [%A - день недели %p - am или pm] (Библиотека time)

#print(html.escape("This HTML contains a &alt;script&gt;script&lt;/script&gt; tag."))  # Преобразование разметки в экранированный текст
#print(html.unescape("I &hearts; Pyt hon's &lt;standart library&gt;."))  # и обратно

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
