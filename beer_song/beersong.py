################  ENG VERSION  ##################
word = 'bottles'
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = 'bottle'
        print(new_num, word, "of beer on the wall")
        print()
print("Go to the store and buy some more, 99 bottles of beer on the wall.")

    ################  RUS VERSION  ##################

# word = 'бутылки'
# for beer_num in range(99, 0, -1):
#     print(beer_num, word, "пива на стене.")
#     print(beer_num, word, "пива.")
#     print("Возьми одну.")
#     print("Выпей до дна.")
#     if beer_num == 1:
#         print("Нет больше бутылок на стене.")
#     else:
#         new_num = beer_num - 1
#         if new_num >= 11 and new_num <= 19:
#             word = 'бутылок'
#             print(new_num, word, "пива на стене.")
#         else:
#             if new_num % 10 == 1:
#                 word = 'бутылка'
#             elif new_num % 10 in (2, 3, 4):
#                 word = 'бутылки'
#             else:
#                 word = 'бутылок'
#             print(new_num, word, "пива на стене")
#     print()
