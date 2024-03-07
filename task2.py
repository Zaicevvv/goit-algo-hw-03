from random import randint

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    print(min >= quantity >= max)
    if type(min) != int or type(max) != int or type(quantity) != int:
        print('All values must be integer')
    elif min < 1 or max > 1000:
        print(f"Values of min:{min} and max:{max} does not match format " \
              "min >= 1 and max <= 1000")
    elif not 0 < quantity < max:
        print(f"Quantity:{quantity} should be in range of " \
              f"min:1 and max:{max - 1}")
    else:
        while len(random_numbers) < quantity:
            random_numbers.add(randint(min, max))

    return sorted(list(random_numbers))
        
print(get_numbers_ticket(1, 49, 49))