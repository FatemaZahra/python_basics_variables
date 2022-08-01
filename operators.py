# ##### Comparison operators
# - `>` greater than
# - `<` less than
# - `==` equals
# - `!=` not equals
# - `>=` greater than equals
# - `<=` less than equals

# a = 4
# b = 2
# print(a > b) #true
# print(a < b) #false
# print(a == b) #false
# print(a !=b) #true
# print(a*b) #8

# functions methods builtin python
greeting = "Hello World!"

# What options are available in pythons built-in library
print(greeting)
# if we wanted to check if the letters are in string
print(greeting.isalpha()) #false

#is it in lowercase, uppercase or mixed
print(greeting.islower()) #false
print(greeting.isdigit()) #false
print(greeting.endswith("!"))
print(greeting.startswith("H")) #case-sensitive

greeting = "Hello World!"
#           01234567891011
#                       -1
print(len(greeting))
print(greeting[-5])
print(greeting[:5])

#print only world in a print statement using slicing
print(greeting[6:11])
# print 4th letter from left to right
print(greeting[:3])
#print 7 letter from right to left
print(greeting[:-7:-1])
#print 6 letter from left to right
print(greeting[:5])

example_string = "Jane                      "
print(example_string)
print(len(example_string))
#strip
print(len(example_string.strip()))

#welcome user with their name and welcome message - name & message start with capital
example_text = "here's some text with lot's of text"
print(example_text.count("text"))

#find a method to bring the statement in capital/small and then first letter in capital
print(example_text.upper())
print(example_text.lower())
print(example_text.capitalize())

# how to replace text within the string
print(example_text.replace("with",","))