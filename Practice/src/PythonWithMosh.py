# print("i am favour")
# print("o----")
# print(" |||| ")
# an expression is a pieces of code that produces a value
# print("*" * 10)

# variables
# this is how we define variable
# price = 10
# rating = 4.9
# name = "favour"
# is_published = False
# print(price)
# full_name = "john pual"
# age = 20
# is_new = True
# when ever we have this function it simply means we are calling or executing this function
# name = input("what is your name? ")
# print("Hi" + name)

# birth_year = input("Birth year:")
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input("weight (lbs):")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

course = "python's course for beginners"
course = 'python for "beginners" '

course = '''
Hi charlie,
Here is my first email to you.
how is your parent,hope every one is fine.
have really missed our childhood's play.
thanks for everything.

'''
# int = [0, 1, 2, 3, 4, 5]
# course = 'python for Beginners'
# print(course[-1])
# print(course[0:])
# print(course[:5])
# print(course)
# course = 'python for Beginner'
# another = course[:]
# print(another)

# name = 'favour'
# print(name[1:-1])

# # want to code john smith is a coder
# first = 'john'
# last = 'smith'
# # Message = first + '[' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg )

# string methods
# course: str = 'python for beginners'
# print(len(course))
# print(course.upper())


String = 'python for "beginners" '

myTexts = '''
 Hi charlie,
 Here is my first email to you.
how is your parent,hope every one is fine.
have really missed our childhood's play.
thanks for everything.

'''
# String = str.split(String)

splitString = myTexts.split()
print(splitString)

dict
inputDictionary = {'Hi charlie': 0, 'how is my first email to you': 1, 'how is your parent,hope everyone is fine': 2,
                   'have really missed our childhood play': 3, 'thanks for everything': 4}
# converting input dictionary items(key-value pair)
# to a list of tuples
resultList = list(inputDictionary.items())
# printing the resultant list of a dictionary
print(resultList)
