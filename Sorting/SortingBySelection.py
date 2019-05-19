def find_smallest_element(item_list: list) -> int:
    """Function which help find smallest index in the list"""
    smallest_element = item_list[0]
    smallest_index = 0
    for i in range(len(item_list)):
        if item_list[i] < smallest_element:
            smallest_element = item_list[i]
            smallest_index = i
    return smallest_index


def selection_sort(item_list: list) -> list:
    """Selection Sort"""
    new_list = []
    for i in range(len(item_list)):
        smallest = find_smallest_element(item_list)
        new_list.append(item_list.pop(smallest))  # Pop() used to delete smallest items in list
    return new_list

