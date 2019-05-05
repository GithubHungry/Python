phase = "Don`t panic!"
plist = list(phase)

print(phase)
print(plist)

new_phase = ''.join(plist[1:3:1])  # Выделяет on из plist
new_phase = new_phase + ''.join([plist[5], plist[4], plist[7], plist[6]])  # К on присоединяются еще ' ','t','a','p'
#  + это конкатенация строк
#  Параллельтно все преобразовывается в строку

print(plist)
print(new_phase)  # Вывод преобразованного в строку массива