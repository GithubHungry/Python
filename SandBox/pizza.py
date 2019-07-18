def making_pizza(size, *toppings):
    """Print size and toppings """
    print("Making a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("\t-" + topping)


