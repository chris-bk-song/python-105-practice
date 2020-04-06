groceries = ['Milk', 'Bread', 'Beer', 'Cheese', 'Bacon']
completed = [False, False, True, True, False]
indexes = range(len(groceries))
for i in indexes:
    that_item = groceries[i]
    did_get_that_item = completed[i]
    if did_get_that_item == True:
        print(f'{that_item}: ✅')
    else:
        print(f'{that_item}: ✔️')