def search_for_vowels(word):
    """Выводит найденные гласные в переданной строке"""
    vowels = set('a,o,e,i,u,y')
    found = vowels.intersection(set(word))
    founded = list(found)
    return founded


print(sorted(search_for_vowels(str(input('Введите строку для анализа:')))))
