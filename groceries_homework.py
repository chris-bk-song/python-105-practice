groceries = []

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''

while True:
    menu_choice = int(input(main_menu))

    if menu_choice == 1:
        print(groceries)
        

    elif menu_choice == 2:
        while True:
            item = input('What do you need from the store? ')
            if item == '':
                break
            groceries.append(item)
        print(groceries)


    elif menu_choice == 3:
        print(groceries)
        start_index_to_replace = int(input('What start index to replace? '))
        end_index_to_replace = int(input('What end index to replace? '))

        if start_index_to_replace == end_index_to_replace:
            new_item = input('What is the new item? ')
    
            groceries[start_index_to_replace] = new_item
        else:
            replacements = []
            while True:
                new_item = input('What is the new item? ')
                if new_item == '':
                    break
                replacements.append(new_item)
                print(replacements)
            groceries[start_index_to_replace:end_index_to_replace] = replacements
            print(groceries)

    elif menu_choice == 4:
        print(groceries)
        start_index_to_delete = int(input('What start index to delete? '))
        end_index_to_delete = int(input('What end index to delete? '))
        
        del groceries[start_index_to_delete : end_index_to_delete]
        print(groceries)

    elif menu_choice == 5:
        break

print('Thank you for using the grocery list app!')
