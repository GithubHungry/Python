def binary_search(itemlist: list, item: int) -> int:
    """Casual binary search"""
    low = 0
    high = len(itemlist) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
    return None
