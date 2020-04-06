groceries = ['Milk', 'Bread', 'Beer'] # One set of grocery list
groceries2 = ['Cheese',  'Churos'] # Another set of grocery list
groceries.extend(groceries2) # Extend grocery list by combining groceries and groceries2
print(groceries) # Display new combined grocery list

groceries3 = ['Chicken', 'Steak'] # You can keep on adding new list
groceries.extend(groceries3)
print(groceries)

# OR bottom works as well

# groceries = ['Milk', 'Bread', 'Beer'] # One set of grocery list
# groceries2 = ['Cheese',  'Churos'] # Another set of grocery list
# groceries3 = ['Chicken', 'Steak'] # One more set of grocery list
# groceries.extend(groceries2 + groceries3) # Extend grocery list by combining groceries and groceries2
# print(groceries) # Display new combined grocery list
