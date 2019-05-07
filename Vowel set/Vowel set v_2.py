vowel = ['a', 'o', 'e', 'u', 'y', 'i', 'A', 'O', 'E', 'U', 'Y', 'I']
word = input("Provide a word to search for volwes: ")

founded = {}  # Пустой словарь

# founded['a'] = 0  # Инициализируем словарь начальными значениями
# founded['o'] = 0
# founded['e'] = 0
# founded['u'] = 0
# founded['y'] = 0
# founded['i'] = 0
# founded['A'] = 0
# founded['O'] = 0
# founded['E'] = 0
# founded['U'] = 0
# founded['Y'] = 0
# founded['I'] = 0

# for k in sorted(founded):  # Вывод из словаря в.1 (sorted - сортирует словарь по ключу), (проходит по ключам словаря)
#     print(k, 'Выводится', founded[k], 'раз.')  # founded[k] - выводит привязанное к ключу значение

for letter in word:  # Проходим по каждой букве введенного слова
    if letter in vowel:  # Если буква встречается в нашем словаре

        #  founded[letter] += 1  # Увеличиваем счетчик на 1
        # if letter in founded:
        #     founded[letter] += 1
        # else:
        #     founded[letter] = 1

        founded.setdefault(letter, 0)  # Setdefault гарантирует нам инициализацию несуществующих ключей(вместо 'banana')
# может быть любое значение, в т.ч. и переменная (н-р в цикле for)
        founded[letter] += 1  # Увеличивает счетчик переменной в словаре под ключом letter на 1

for k, v in sorted(founded.items()):  # founded.item() - возвращает список пар ключ/значение (ПРЕДПОЧТИТЕЛЬНЕЕ)
    # sorted(dictionary) - сортирует словарь (по ключам?)
    print(k, 'использовалось', v, 'раз(a).')
