import json

with open('numbers.json') as file_obj:
    numbers = json.load(file_obj)
for num in numbers:
    print(num)
