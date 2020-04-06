# To fill the grocery list:
# -Prompt until they enter empty string
# Show them the list
# -That is, print() it!
# Give them a chance to replace stuff in list
# -Prompt for a subset of items to replace
#   -If start and end same, replace 1
#   -If different, replace with a list
#       -(Prompt until they enter empty string)

groceries1 = []

while True:
        item = input('What do you need from the store? ')

        if item == '':
            break
        groceries1.append(item)

indexes = range(len(groceries1))
for i in indexes:
    item = groceries1[i]
    print(f'{i}: {item}')

start_index_to_replace = int(input('What start index to replace? '))

end_index_to_replace = int(input('What end index to replace? '))

if start_index_to_replace == end_index_to_replace:
    new_item = input('What is the new item? ')
    
    groceries1[start_index_to_replace] = new_item
else:
    replacements = []
    while True:
        new_item = input('What is the new item? ')
        if new_item == '':
            break
        replacements.append(new_item)
        print(replacements)
    groceries1[start_index_to_replace:end_index_to_replace] = replacements

for i in indexes:
    item = groceries1[i]
    print(f'{i}: {item}')