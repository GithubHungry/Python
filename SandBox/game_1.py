import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада', 'прогноз',
              'галька')

secret_word = random.choice(words_list)
print(secret_word)

gamers_word = ['*'] * len(secret_word)  # делаем из строки список элементов длины secret_word
print(' '.join(gamers_word))

# gamers_word[1] = 'к'
# print(' '.join(gamers_word))

errors_counter = 0
while True:
    letter = input('Введите одну букву: ').lower()
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for position, symbol in enumerate(secret_word):
            if symbol == letter:
                gamers_word[position] = letter
        if '*' not in gamers_word:
            print("you win")
            print("Было загадано слово: " + str(secret_word))
            break
    else:
        errors_counter += 1
        print('\tОшибок допущено: ' + str(errors_counter))
        if errors_counter == 8:
            print('You lose(')
            break

    print(' '.join(gamers_word))
