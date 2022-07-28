# testing the env with pycharm using python 3.10.5
# print("Fatema")

# What are variable
#variable is to help us store data of different types
# name = "Fatema 20 + 5" #string
# age = 25 #int
# salary = 19.5 #float
#
# print(name)
# print(age)
# print(salary)
# # Types of variable
# #int, floats 5.5, boolean true false,string
#
# print(type(name))
# print(type(age))
# print(type(salary))

# #take user input with method called input()
# print("Please enter your name")
# name = input()
# print("Welcome")
# print(name)

#create var input for first_name, last_name, age, address, salary, course
#it should start with Hi & welcome message
#it needs to be printed back to the user
#print the type of each var

print("Hi, Welcome Aboard! Please enter your first name")
first_name = input()
print(type(first_name))
print("Hi "+ first_name + "! Please enter your last name")

last_name = input()
print(type(last_name))
print("Thank you for your name. "+first_name +" "+last_name+". Please share your age.")

age = int(input())
print("Your age is"+ " ")
print(age)
print(type(age))

print("Please enter your address")
address = input()
print("Your address is:"+ address)
print(type(address))

print("Please enter your salary")
salary = float(input())
print("Your salary is:")
print(type(salary))

print("Please enter your course")
course = input()
print("Your course is:"+ course)
print(type(course))

