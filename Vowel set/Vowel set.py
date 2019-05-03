vowel = ['a', 'o', 'e', 'u', 'y', 'i', 'A', 'O', 'E', 'U', 'Y', 'I']
founded = []
word = input("Provide a word to search for volwes: ")
for letter in word:
    if letter in vowel:
        if letter not in founded:
            founded.append(letter)
            # print(len(founded))  # help to count numbers of correct letter
for perem in founded:  # Тупо перебор элементов массива найденных уникальных гласных
    print(perem)
