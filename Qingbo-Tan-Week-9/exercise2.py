import random
from exercise1 import display_solution
from exercise1 import find_best_combination

names = {
    'ring',
    'watch',
    'coins',
    'vase',
    'painting',
    'statue',
    'lamp',
    'book',
    'bottle',
    'sculpture',
    'cards',
    'gun',
    'medal',
    'stamp',
    'doll'
}

qualifiers = {
    'old',
    'ancient',
    'special',
    'rare',
    'unique',
    'small',
    'large',
    'tiny',
    'big',
    'huge',
    'classic',
    'art deco',
    'modern',
    'vintage',
    'antique'
}


def create_item_name(qualifiers, name):
    # create a random name for the item
    item_name = random.choice(list(qualifiers)) + ' ' + random.choice(list(names))
    return item_name


def generate_items(n):
    items = {}
    while len(items) < n:
        item = {
            'name': create_item_name(qualifiers, names),
            'value': random.randint(1000, 5000),
            'size': random.randint(1, 5)
        }
        if item['name'] not in items:
            items[item['name']] = item
    return items.values()

max_size = 100
for size in range(2, max_size + 1):
    print(f'Generating items with size = {size}:')
    items = generate_items(size)
    # use the naive solution to find the best combination of items
    solution = find_best_combination(items, 10)
    print('Naive solution:')
    display_solution(solution)
    print()