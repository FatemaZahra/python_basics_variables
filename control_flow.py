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
# print only keys
print(dictionary.keys())
# print only values
print(dictionary.values())
# use for loop to iterate through it
for keys, values in dictionary.items():
    # print key with matching value
    print(keys, values)

# use case of multiple conditions
# create a list with int values 1-4
data_list = [1, 2, 3, 4]
# iterate through the list using for loop
for number in data_list:
    # find 3 and print if found
    if number == 3:
        print("found 3")
    # or else list number greater than 3 print gone too far
    elif number > 3:
        print("gone too far")
     # otherwise print too soon
    else:
        print("too soon")

# while loop?
# while loops are mostly used as a monitor rather than handling items

number = 0
# iterate while number is less than 10
while number < 10:
    # print the number with message stating it's working
    print(f"its working --> {number}")
    # add +1 in each iteration
    number += 1





