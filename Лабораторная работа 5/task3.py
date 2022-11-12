import random

def unique_numbers():
    numbers = random.sample(range(-11,11), 16)
    return numbers

list_unique_numbers = unique_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


