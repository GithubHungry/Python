def search_for_letters(letters: set, phase: str) -> set:
    """Возвращает найденные буквы множеством в переданной строке"""
    # vowels = set('aoeiuy')
    # print(type(vowels))
    # found = vowels.intersection(set(word))
    # founded = list(found)
    # return found
    # return bool(founded)
    return letters.intersection(set(phase))


def search_for_letters_v_2(phase: str, letters: str = 'aoiuye') -> set:
    return set(letters).intersection(set(phase))


setter = set('aoiue')
print(search_for_letters(setter, str(input('Введите строку для анализа:'))))
print(search_for_letters_v_2(str(input('Введите строку для анализа:')), str(input("Введите то,что мы будем искать"))))
print(search_for_letters_v_2(str(input("Введи:"))))
