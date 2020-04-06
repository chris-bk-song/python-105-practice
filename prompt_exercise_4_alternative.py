groceries1 = []

while len(groceries1) < 3:
    item = input('What do you need from the store? ')
    groceries1.append(item)

groceries2 = []

while len(groceries2) < 3:
    item = input('What do you need from the store? ')
    groceries2.append(item)

groceries1.extend(groceries2)

print(groceries1)

indexes = range(len(groceries1))
for i in indexes:
    item = groceries1[i]
    print(f'{i}: {item}')

replace_index = int(input('Please provide index of the item on your list to be replaced [0-5]: '))

replace_item = input('Please provide the name of the new item to be replaced: ')

groceries1[replace_index] = replace_item

print(groceries1)