# prompt the user for a single grocery item
#   - append it to the 'groceries' list
# in an infinite while loop, prompt the user for an item
#   - append the item to the list
#   - print() the list after you add the line
# (To exit out of the loop, press Ctrl C)


# Correct way

groceries = []

while True:
    grocery_item = input('Please enter a grocery item: ')

    groceries.append(grocery_item)

    print(groceries)

# Wrong way (It will only display one item for my list)

# while True:
#    groceries = []
#    grocery_item = input('Please enter a grocery item: ')
#
#    groceries.append(grocery_item)
#
#    print(groceries)


