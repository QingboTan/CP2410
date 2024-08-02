from exercise2 import generate_items
from exercise2 import display_solution


#The worst-case time complexity is O(n*W), where W is refered to maximum size
def knapsack(items, max_size):
    # Create the dynamic programming grid
    grid = [[0 for _ in range(max_size + 1)] for _ in range(len(items) + 1)]
    # Populate dynamic programming grid
    for i in range(1, len(items) + 1):
        item_value = items[i - 1]['value']
        item_size = items[i - 1]['size']
        for j in range(1, max_size + 1):
            # If the item can't fit, carry over the value from the cell above
            if item_size > j:
                grid[i][j] = grid[i - 1][j]
            else:
                # If the item can fit, choose the maximum value between:
                # - The value of the current item + the value of the remaining column from the previous row
                # - The value from the cell directly above
                grid[i][j] = max(item_value + grid[i - 1][j - item_size], grid[i - 1][j])
    # find the selected items
    selected_items = []
    i = len(items)
    j = max_size
    while i > 0 and j > 0:
        if grid[i][j] != grid[i - 1][j]:
            selected_items.append(items[i - 1]['name'])
            j -= items[i - 1]['size']
        i -= 1
    # return the maximum value that can fit into the knapsack and the selected items
    return grid[-1][-1], selected_items

max_size = 225
for size in range(2, max_size + 1):
    print(f'Generating items with size = {size}:')
    items = generate_items(size)
    display_solution(items)
    print()

    best_value, selected_items = knapsack(items, size)
    print('Dynamic programming solution:')
    print(f'Best value: {best_value}')
    print(f'Selected items: ', end='')
    print(*selected_items, sep=', ')
    print()
