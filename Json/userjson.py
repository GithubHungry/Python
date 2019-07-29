import json

try:
    with open('username.json', 'r') as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    with open('username.json', 'w') as file_obj:
        name = input('Please, enter your username: ')
        json.dump(name, file_obj)
        print('We will remember you ' + name + '!')
else:
    print("Welcome back! " + username.title())
