# with open('pi_digits.txt') as file_obj:
#     spis = file_obj.readlines()
# text = ''
# for line in spis:
#     text += line.rstrip()
#     # print(line.rstrip())
# my_bd = input("Please, enter your birthday date: ")
# if my_bd in text:
#     print('Yes')
# else:
#     print("No(")

# content = file_obj.read()
# for line in file_obj:
#     print(line.rstrip())

# with open('pi_digits.txt') as file:
#     text = file.readlines()
# message = ''
# for line in text:
#     message += line.rstrip() + '. '
# print(message)
# new_message = ''
# for line in text:
#     new_message += line.replace('Python', 'JS').rstrip() + '. '
# print(new_message)

# with open('pi_digits.txt', 'w') as file_obj:
#     # file_obj.write("Hi, yes,yes it`s me!")
#     file_obj.write(str(1488))

with open('pi_digits.txt', 'a') as file_obj:
    while True:
        current_name = input("Please, enter your name: ")
        if current_name != 'Quit':
            file_obj.write(current_name + '\n')
            print('Success!')
        else:
            print('Bye!')
            break
