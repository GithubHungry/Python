vowels = set('aoeiuyAOEIUY')
word = str(input("Введите строку"))
print(vowels)
print(word)
i = vowels.intersection(set(word))
for vowel in i:
    print(vowel)
