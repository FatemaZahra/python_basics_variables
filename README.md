# python_basics_variables
## To install python follow the steps
Download the latest version of python using the following link: [Python download](https://www.python.org/downloads/)

![Screenshot 2022-07-28 at 17 29 03](https://user-images.githubusercontent.com/102330725/181590027-3a9406a5-fe5c-4f7f-a172-44b70134869c.png)
_Note: The link automatically opens up for the operating system you are on. So do not worry!_

Once downloaded 

**Step 1:** Open file

**Step 2:** Add Python to PATH by ticking the box at the bottom as shown in the image.

<img width="1065" alt="Screenshot 2022-07-28 at 17 31 25" src="https://user-images.githubusercontent.com/102330725/181590413-d774693a-cadd-41a0-8c81-380be7d4c6ad.png">

**Step 3:** Click install

Once installed,
Open the shell and tyep in the code below:

```
python --version
```


## To setup Pycharm follow the link

**For windows:** [Pycharm windows download](https://www.jetbrains.com/pycharm/download/#section=windows)

**For macOs:** [Pycharm Mac download](https://www.jetbrains.com/pycharm/download/#section=mac)

**For Linux:** [Pycharm Linux download](https://www.jetbrains.com/pycharm/download/#section=linux)

![Screenshot 2022-07-28 at 17 40 56](https://user-images.githubusercontent.com/102330725/181592162-c7742535-60dc-4247-bbd8-430507a4bcbc.png)

**Please ensure to download the Community version**

Next steps:
- Double click the downloaded file
- Drag and Drop in the Applications Folder

![Screenshot 2022-07-28 at 17 45 03](https://user-images.githubusercontent.com/102330725/181592998-85222f61-5b96-4f86-802f-11dc3b56512c.png)


_Note: Always run Pycharm as an administrator_

## Introduction to Python
Python is a computer programming language often used to build websites and software, automate tasks, conduct data analysis and perform many more tasks. It is also an open-source and multi-platform language.

### What are variables?
A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.

### Variable Types
- int
- float
- string
- boolean
- list
- dictionary

### The following code can be used to print the type of variable
```
name = input()
print(type(name))
```
### Commands to push a repository

`git add . `

`git commit -m "message"`

`git push -u origin main`

### Data types and operators
#### Two types of operators

##### Arithmetic operators
- `+ - * /`
- `+` adds two operands (var) together
- `-` subtract
- `*` multiply
- `/` divide

##### Comparison operators
- `>` greater than
- `<` less than
- `==` equals
- `!=` not equals
- `>=` greater than equals
- `<=` less than equals

```python
print(a > b) #true
print(a < b) #false
print(a == b) #false
print(a !=b) #true
print(a*b) #8
```

## Built-in methods
```python
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
```
#### Strings Concatenation Casting
- String indexing
- `Hello World!`
- Index in python starts with 0

- Hello World!
  01234567891011

```python
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
```

# Data Collections
## Lists, Tuples & Dictionaries
### Lists
What are lists?
Correct Syntax []
lists are mutable
indexing same concept applies

```python

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

```