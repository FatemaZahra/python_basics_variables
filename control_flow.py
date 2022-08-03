# if elif and else
# loops - for and while loops
# not to repeat yourself
# loops help us to ITERATE through datat collections - DATA
# let's create a list to use for loop to iterate through

shopping_list = ["fruits", "milk", "cream", "bread"]
# print(shopping_list)
# print each item of the list as a list
# fruits
# milk
# cream
# bread
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

for item in shopping_list:
    print(item)
    #does the list have bread
    # if bread is found in the list stop the progress
    if item == "milk":
        break

# create a dictionary with 6 key value pairs
dictionary = {
    "name": "Fatema",
    "fav_colour": "white",
    "hobbies": "painting",
    "likes": "coding",
    "from" : "India",
    "lives" : "UK"
}
print(dictionary.keys())
print(dictionary.values())
# use for loop to iterate through it
for keys, values in dictionary.items():
    print(keys, values)

# print only keys
# print only values
# print key with matching value
