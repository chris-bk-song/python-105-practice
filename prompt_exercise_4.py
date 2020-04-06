groceries1 = []
while len(groceries1) < 3:
    item = input('What do you need from the store? ')
    groceries1.append(item)

groceries2 = []
while len(groceries2) < 3:
    item = input('What do you need from the store? ')
    groceries2.append(item)

# Option 1: Combine two grocery lists above
groceries1.extend(groceries2)

# Option 2: Combine two grocery lists above
# groceries3 = groceries1 + groceries2

# Print the combined grocery list
print(groceries1)

# Prompt the user for the index of the item to replace
replace_index = int(input('Please provide index of the item on your list to be replaced [0-5]: '))

# Prompt the user for the new item
replace_item = input('Please provide the name of the new item to be replaced: ')

# Replace the item at that index with the new item
groceries1[replace_index] = replace_item

# Print the updated combined list
print(groceries1)

# OR
# indexes = range(len(groceries1))
# for item in groceries1:
#   print(f'{1}: {groceries1[item]}')
# replace_index = int(input('Please provide index of the item on your list to be replaced [0-5]: '))
# replace_item = input('Please provide the name of the new item to be replaced: ')
# groceries1[replace_index] = replace_item
# print(groceries1)