from random import randint

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    
    if type(min) != int or type(max) != int or type(quantity) != int:
        print('All values must be integer')
    elif min < 1 or max > 1000:
        print(f"Values of min:{min} and max:{max} does not match format " \
              "min >= 1 and max <= 1000")
    elif not 0 < quantity <= max or quantity > (max - min + 1):
        print(f"Quantity:{quantity} should be in range of " \
              f"1 and max:{max} and shouldn't be grater " \
              f"than max-min+1:{max - min + 1}")
    else:
        while len(random_numbers) < quantity:
            random_numbers.add(randint(min, max))

    return sorted(list(random_numbers))
        
print(get_numbers_ticket(1, 2, 2))