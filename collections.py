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

# Tuples
## Why do we need Tuple?
# Lists [] are mutable Vs Tuples () are immutable
# syntax for tuple ()
# What are the use cases?
essential = ("city", "DOB", "place of birth")
#             0        1        2
print(essential)
print(type(essential))
print(essential[1])
## essential[0] = "town" #immutable

#essential ()
#essential []
#essential {} Dictionary

# What is a Dictionary {} ?
# Dictionary can have all types of data collection
# Dictionary works as "KEY": "VALUE" pair

devops_student_1 = {
    "key": "value",
    "name": "James",
    "stream": "tech",
    "completed_lessons": 3,
    "completed_lessons_names": ["lists", "operations", "built-in methods"]
}
print(devops_student_1)
print(devops_student_1.keys())
print(devops_student_1.values())
# print(type(devops_student_1))
# print(devops_student_1["name"])
# find out how to delete in items from dict and delete operations
del devops_student_1["name"]
print(devops_student_1)
# find out how to change completed lesson from 3 to 2
devops_student_1["completed_lessons"] = 2
print(devops_student_1)