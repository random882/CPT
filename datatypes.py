"""
There are two type of dataypes, scalar and collections.

scalar datatypes are: int, float, boolean and str
collections are: list and dict
"""

# After each exercise print the name of the variable and the value.
# Example: print("foo", foo)


############################
##### Scalar Exercises #####
############################

"""
int : Integers are positive and negative whole numbers.  Like -5, 0, 34, etc.
"""

# Excercise 1: create an integer variable named age to store how old you are, and then print it
age = 16
print("age",age)

# Excercise 2: create an integer variable named tenbelow that holds a negative value, and then print it
tenbelow = -4
print("tenbelow", tenbelow)

# Excercise 3: create an integer variable named zero, and then print it
zero = 0
print("zero",zero)

"""
float :  Floats are positive and negative decimal numbers. Like -23.75, 0.0, 36.42, etc
"""

# Excercise 4: create a float variable named pi, and then print it
pi = 3.14
print("pi",pi)
# Excercise 5: create a float variable named debt that holds a negative value, and then print it
debt = -42
print("debt",debt)

# Excercise 6: create a float variable named zerof, and then print it
zerof = -34.1
print("zerof",zerof)

"""
bool :  Booleans only store one of two values True, False
"""

# Excercise 7: create a boolean variable named theskyisblue, and then print it
theskyisblue = True
print("Is the sky blue?",theskyisblue)

# Excercise 8: create a boolean variable named theskyisred, and then print it
theskyisred = False
print("Is the sky red?",theskyisred)

"""
str :  Strings are values in quotes
"""

# Excercise 9: create a string variable to store your nickname, and then print it
nickname = "Aiden"
print("Your name is",nickname)


#################################
##### Collections Exercises #####
#################################

"""
list :  The items in a list maintain a specific order, called the index, usually starting at 0. 
The value stored at an index can be a scalar value or another collection.

This collection is similar to what other languages call an Array.

Creating a List:
You create a list by enclosing a comma-separated sequence of items within square brackets []
example: colors = ["red", "green", "blue"]

Accessing Items:
You can access individual items using their index within square brackets. 
example: colors[1]

Mental Model Of A List In Computer Memory:
-------------------
| index | value   |
-------------------
|   0   | "red"   |
-------------------
|   1   | "green" |
-------------------
|   2   | "blue"  |
-------------------
"""

# Excercise 10: create a list of integers from 10 to 0 named countdown, and then print it
countdown = ["10","9","8","7","6","5","4","3","2","1","0"]
print("countdown",countdown)

# Excercise 11: create a list of floats named prices, and then print it
prices = ["46.2","44.3","16.1"]
print("prices",prices)
# Excercise 12: create a list of fruits, and then print it
fruits = ["orange","Mango","Apple","Grape"]
print("fruits",fruits)
# Excercise 13: create a list named firsts that stores the first value of each of the lists you created, and then print it
firsts = [countdown[0],prices[0],fruits[0]]
print("firsts",firsts)

"""
dict :  The items in a dictionay are stored similar to a list, but instead of indexes, key-value pairs are used.
The value stored at a key can be a scalar value or another collection.
The keys are strings.

this collection is similar to what other laguages call a HashMap.

Creating a Dictionary: 
Dictionaries are created using curly braces {} with key-value pairs separated by colons : and individual pairs separated by commas ,
example:
player = {
  "speed": 50, 
  "damage": 2.5, 
  "weapons": ["sword", "axe"],
}

Accessing Items:
You can access individual items using their key within square brackets. 
example: player["weapons"]

Mental Model Of A Dictionary In Computer Memory:
--------------------------------
|  key      | value            |
--------------------------------
| "speed"   | 50               |
--------------------------------
| "damage"  | 2.5              |
--------------------------------
| "weapons" | ["sword", "axe"] |
--------------------------------
"""

# Excercise 14: create a dict named me with the following keys: name, age, hobbies, and then print it
identity = {
    "name": "Aiden", 
    "age": 17,
    "hobbies": ["video games","Skating","Basketball","Baseball"]
}
print("identity",identity)
# Excercise 15: create a variable named funstuff that is the list of your hobbies, and then print it
funstuff = identity["hobbies"]
print("funstuff",funstuff)