# Data Collections
## Lists, Tuples & Dictionaries
### Lists
# What are lists?
# Correct Syntax []
# lists are mutable
# indexing same concept applies
#
shopping_list = ["bat", "milk", "bread" ]
#                 0        1       2
print(shopping_list)

#find out the type of shopping list

print(type(shopping_list))

# find out the len of shopping list

print(len(shopping_list))

# how to add to our shopping list
shopping_list.append("oreos") # append() adds an item at the end of the list

print(shopping_list)

# how to delete an item from our shopping list
shopping_list.remove("milk")
print(shopping_list)

#find out to replace an item from the list back with milk

mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)

#print 2 and 3 from the above list
print(mixed_list[1]) # outcome would be 2
print(mixed_list[2]) # outcome would be 3
print(mixed_list[1:3]) # outcome would be 2,3
print(mixed_list[-1:])