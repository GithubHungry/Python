from Test_learning.name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Please, enter your first name:")
    if first == 'q':
        break
    second = input("Please, enter your second name:")
    if second == 'q':
        break
    print(get_formatted_name(first, second))
