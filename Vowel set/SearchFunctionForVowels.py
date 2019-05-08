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
    """Функция по поиску набора букв в передаваемой строке"""
    return set(letters).intersection(set(phase))


def binarysearch(arr: list, guess: int) -> int:
    """Функция бинарного поиска в списке, с возвратом позиции найденного элемента"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        tr = arr[mid]
        if guess == tr:
            print('yes')
            return mid
        if tr > guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


# setter = set('aoiue')
# print(search_for_letters(setter, str(input('Введите строку для анализа:'))))
# print(search_for_letters_v_2(str(input('Введите строку для анализа:')), str(input("Введите то,что мы будем искать"))))
# print(search_for_letters_v_2(str(input("Введи:"))))
# print(search_for_letters_v_2(phase=str(input('введи строку')), letters='eo'))
# print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
