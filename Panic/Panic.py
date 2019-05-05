phase = "Don`t panic!"
plist = list(phase)
print(phase)
print(plist)

########## Мой вариант ##########

# spis = ['D', '`', ' ', 'i', '!']  # Вспомогательный список для удаления
# for letter in plist:  # роход по списку с удалением совпадений
#     if letter in spis:
#         plist.remove(letter)
# plist.pop(5)  # Удаляется вторая буква n
# plist.pop()  # Удаляется буква c последняя  --?
# plist.append('p')  # Добавляется в конец буква р
# plist.remove('p')  # Удаляется буква р первая --?
# plist.insert(2, ' ')  # Добавляется пробел после on

########## Книжный вариант ##########

for i in range(4):
    plist.pop()  # Удаляет с КОНЦА
plist.pop(0)  # Удаляет первый символ в списке
plist.remove('`')
# plist.insert(3,plist.pop(2))
# plist.insert(6,plist.pop(4))
plist.extend([plist.pop(), plist.pop()])  # Сперва извлекает 2 последние буквы, затем вставляет их в конец ([] - важно)
plist.insert(2, plist.pop(3))  # Извлекает пробел, а затем его вставляет

########## Книжный вариант (см. Panic_v_2.py)##########
# new_phase = ''.join(plist[1:3:1])  # Выделяет on из plist
# new_phase = new_phase + ''.join([plist[5], plist[4], plist[7], plist[6]])  # К on присоединяются еще '','t','a','p'

new_phase = ''.join(plist)  # Преобразует массив в строку
print(plist)
print(new_phase)  # Вывод преобразованного в строку массива
