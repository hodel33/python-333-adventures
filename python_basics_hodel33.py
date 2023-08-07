###   A 333 Line Adventure into Python Basics by Hodel33   ###

# Welcome, future coder! You've embarked on a journey through the fascinating realm of Python.

# In the festive spirit of Christmas 1989, a Dutch programmer named Guido van Rossum had an idea to transform the way we code.
# His dream was to make programming fun, and from that dream, Python was born. His vision was simple: create an intuitive, 
# easy-to-use language that was open-source, allowing coders worldwide to contribute to its growth.
# And the name 'Python'? A tribute to his love for the comedic genius of Monty Python's Flying Circus.

# Python is clean, readable, and above all, enjoyable - making it an ideal starting point for those new to programming!
# In this guide, we'll delve into Python's basics, navigating the landscape with playful analogies.
# Ready for a code adventure across 333 lines? Let's dive in!

# Journey Map:
# 1. Data Types | 2. Variables | 3. Formatted Strings | 4. Data Structures | 5. Data Type Conversion
# 6. Arithmetic Operators | 7. Comparison Operators | 8. Conditional Statements | 9. Loops | 10. Functions



### 1. Data Types
print("\n--- Meet the Data Types ---\n")

# Data types in Python are like different shapes of clay we use to sculpt our programs. First, we give a variable a name 
# and then assign it a value with a simple '='. It's like saying "this piece of clay (the variable) is now a cube (the data type)".

int_var = 10  # An integer: Think of it as a whole number - no fractions here!
float_var = 1.65  # A float: It's like an integer, but more flexible. Fractions allowed!
str_var = "Hello, World!"  # A string: It's text - letters, words, sentences, even emojis! 🐍
bool_var = True  # A boolean: It's like a light switch, it can only be True (On) or False (Off).
none_var = None  # None: It's a special type indicating absence of a value (also known as 'null').

# Now, let's take a look at our freshly sculpted data types!
print("Integer, you're a solid number:", int_var)
print("Float, you've got the balance:", float_var)
print("String, say something:", str_var)
print("Boolean, what's your status?", bool_var)



### 2. Variables
print("\n--- Variables: The Labels of our Data Warehouse ---\n")

# Variables in programming are like labels on boxes in a warehouse, pointing to the data stored inside. 
# We use variables for a few reasons:
# 1. Reusability: Once we label a box (store a value in a variable), we can use it again without needing to make a new box.
# 2. Readability: Descriptive labels (good variable names) make our warehouse (code) easier to navigate.
# 3. Changeability: Variables let us change the contents of a box in one place, affecting all labels pointing to it.

# Variable names should always start with a letter or an underscore, but not with a number, and they must maintain case consistency.
# Let's define some variables:
fav_number = 33
fav_food = "pizza"

# We can use variables to store our data and reference it whenever we need.
print("My favorite number is", fav_number)
print("My favorite food is", fav_food)



### 3. Formatted Strings (f-strings)

# F-strings are like VIP invites for variables, allowing them to party inside text with a simple 'f' prefix and {}.
# It offers a less confusing way to include variables in messages than using ',' or '+'.
print(f"My favorite number is {fav_number} and my favorite food is {fav_food}.")

# F-strings are flexible! They can do simple calculations inside those braces.
print(f"Did you know, 10 times my favorite number is {10 * fav_number}?")

# Now, imagine your f-string is a multi-story party building and you want to go to the next floor.
# The '\n' is your elevator! It moves the party to the next line.
print(f"Welcome to the party!\nMy favorite number is {fav_number}, and my favorite food is {fav_food}.")

# The f-string method is often the clearest and most readable way to include variables within strings, 
# as it handles the conversion for you and doesn't add any extra spaces unless you want them.



### 4. Data Structures
print("\n--- Gather 'round, Data Structures! ---\n")

# Data Structures are like containers for our data, each with its own special properties!

## List
list_var = [1, 2, 3, 4, 5]  # A list: It's like a train, each car (item) follows another in a specific order!
print(f"List, line up!: {list_var} | Passenger count: {len(list_var)}")

# 'len()' is a built-in Python function that gives us the length/count of items (passengers) in a container such as a list.

# Accessing data in a list is like checking which passenger is in a specific train car!
# In Python, we start counting from 0, so the first passenger is at index 0.
print(f"Who's in the first car? It's: {list_var[0]}")

# Adding a passenger to our train is easy too!
list_var.append(6)
print(f"A new passenger arrived! Line up: {list_var}")


## Dictionary
dict_var = {"key1": "value1", "key2": "value2"}  # A dictionary: Think of it as a treasure chest, each key opens a unique treasure!
print(f"Dictionary, what's in the chest?: {dict_var} | Treasure count: {len(dict_var)}")

# Accessing data in a dictionary is like using a key to unlock a piece of treasure!
print(f"What does 'key1' unlock? It's: {dict_var['key1']}")

# But wait, what if we try to unlock a treasure with a key that doesn't exist? 
# That's when we use the '.get' method. It tries to unlock the treasure, and if the key doesn't exist, it just says 'None'!
print(f"What does 'key3' unlock? It's: {dict_var.get('key3')}")

# Adding a treasure to our chest is a breeze!
dict_var["key3"] = "value3"
print(f"A new treasure! Chest contents: {dict_var}")


## Set
set_var = {1, 2, 3, 3, 4}  # A set: It's like a party, everyone is invited but no duplicates allowed!
print(f"Set, party guests: {set_var} | Guest count: {len(set_var)}")


## Tuple
tuple_var = (1, 2, 3, 4)  # A tuple: It's a lot like a list, but once set, it cannot be changed. A list's more committed cousin!
print(f"Tuple, assemble: {tuple_var} | Member count: {len(tuple_var)}")



### 5. Data Type Conversion
print("\n--- Transformation time, Data Types! ---\n")

# Sometimes, to make operations work smoothly, we need to convert (cast) data from one type to another.
# It's like making sure you have the right ingredients for your recipe!

str_to_int = int("123")  # Let's turn a string into an integer!
print(f"String to integer transformation: {str_to_int} | Type: {type(str_to_int)}")

# 'type()' is a built-in Python function that helps us identify what kind of data we're dealing with.
# It's like a name tag for our data - revealing whether it's an integer, float, string, boolean, or something else!

int_to_float = float(10)  # Now, let's change an integer into a float!
print(f"Integer to float transformation: {int_to_float} | Type: {type(int_to_float)}")

# But beware! Not all conversions are possible. Trying to do an impossible conversion is like trying to fit a square peg in a 
# round hole, and it will make our program trip and fall (throw an error). But don't worry, Python has a safety net ready!
try:
    impossible_conversion = int("Hello, World!")  # The daring stunt!
except ValueError:  # The safety net catches us if the stunt fails!
    print("Some transformations just aren't possible!")

# We will talk more about this safety net (Error Handling) in an upcoming guide. Stay tuned!



### 6. Arithmetic Operators
print("\n--- Arithmetic Playground ---\n")

# Arithmetic operators in Python are like the tools in a math toolbox - each one has its own unique function!

## Addition (+)
addition = 10 + 5  # It's a party, and '+' invited 5 to join 10!
print(f"Addition party: {addition}")

## Subtraction (-)
subtraction = 10 - 5  # '-' told 5 to leave the 10 party. Bye, 5!
print(f"Subtraction farewell: {subtraction}")

## Multiplication (*)
multiplication = 10 * 5  # '*' is like a cloning machine. It made 10 copies of 5!
print(f"Multiplication clone army: {multiplication}")

## Division (/)
division = 10 / 5  # '/' divided 10 into 5 equal groups.
print(f"Division split: {division}")

## Floor Division (//)
floor_division = 10 // 3  # '//' is a generous host, but avoids fractions. Serving 3 guests, each got 3 with nothing left.
print(f"Floor Division fairness: {floor_division}")

## Modulus (%)
modulus = 10 % 3  # '%' is the leftovers officer, reporting 1 cookie left after evenly sharing 10 cookies between 3 people!
print(f"Modulus leftovers: {modulus}")

# Now let's talk about the BIDMAS/BODMAS rule, which is the order Python follows to execute operations:
# Brackets/Orders (powers, square roots, etc.), Division/Multiplication (L-to-R), Addition/Subtraction (L-to-R).

# Let's put it to the test!
# Apply BIDMAS: First, solve brackets (15), then multiplication (45), then division (9), and finally subtraction.
bidmas_test = (10 + 5) * 3 / 5 - 2
print(f"BIDMAS challenge: {bidmas_test}")



### 7. Comparison Operators
print("\n--- Join the Comparison, Operators! ---\n")

# Comparison operators are like weighing scales, giving verdicts: True or False.

## Equality (==)
print(f"Equality Test: {10 == 10}")  # 10 and 10 are the same number, so this is True.

## Inequality (!=)
print(f"Inequality Test: {10 != 5}")  # 10 and 5 are different numbers, so this is True.

## Greater than (>) and Less than (<)
print(f"Greater than Test: {10 > 5}")  # 10 is bigger than 5, so this is True.
print(f"Less than Test: {10 < 5}")  # 10 is not smaller than 5, so this is False.

## Greater than or equal to (>=) and Less than or equal to (<=)
print(f"Greater than or equal to Test: {10 >= 10}")  # 10 is equal to 10, so this is True.
print(f"Less than or equal to Test: {10 <= 10}")  # 10 is equal to 10, so this is also True.



### 8. Conditional Statements
print("\n--- Time to make choices, Conditional Statements! ---\n")

# Conditional statements in Python are like road signs, guiding our program on what path to take.

## If Statement
# 'If' is like a weather forecaster. It looks at the weather and decides what to wear.
weather = "sunny"  # Let's define our weather for today.
if weather == "sunny":  # If the weather is sunny...
    print("If Statement: It's sunny, wear sunglasses!")  # ...wear sunglasses!

## Else Statement
# 'Else' is the forecaster's default wardrobe. If it doesn't know the weather, it goes with a safe choice.
weather = "unknown"
if weather == "sunny":
    print("If Statement: It's sunny, wear sunglasses!")
else:  # If the weather is anything else...
    print("Else Statement: Unknown weather, wear a cap just in case!")  # ...wear a cap!

## Elif Statement
# 'Elif' is like having more wardrobe options. It adds more conditions for the forecaster to check.
weather = "rainy"  # Let's change our weather.
if weather == "sunny":
    print("Elif Statement: It's sunny, wear sunglasses!")
elif weather == "rainy":  # If the weather is rainy...
    print("Elif Statement: It's rainy, take an umbrella!")  # ...take an umbrella!
else:
    print("Elif Statement: Unknown weather, wear a cap just in case!")

## If Variable / If not Variable
# Python allows 'if' and 'if not' to be used directly with a variable, no comparison operator needed.
# 'if variable' is True when the variable holds some content, while 'if not variable' checks for empty, None, zero, or False values.
weather = "cloudy"  # Some weather data.
if weather:  # If 'weather' has content...
    print(f"If Variable: Weather is {weather}")

weather = ""  # No weather data.
if not weather:  # If 'weather' has no content...
    print("If not Variable: No weather data available.")



### 9. Loops
print("\n--- Round and Round, Loops! ---\n")

# Loops are like a merry-go-round. They keep going until someone stops them! This makes them incredibly useful in programming
# as they allow us to automate repetitive tasks efficiently, saving us time and making our code cleaner and easier to read.

## For Loop
# It's like a dance routine - we do it for a set number of times!
for step in range(1, 5):  # range(1, 5) generates a sequence starting from 1 (Start) up to but not including 5 (Stop).
    print(f"For Loop Dance, step: {step}")

# For Loop with (Start, Stop, Step)
# It's like setting an alarm clock - we start at a certain time, end before a particular time, and we can skip (Step) some hours!
for hour in range(2, 10, 2):  # We set the alarm to start at 2, to end before 10, and to ring every 2 hours!
    print(f"For Loop Alarm Clock, hour: {hour}")

# For Loop through a List
# It's like a checkout line - each item gets its turn!
shopping_cart = ["apple", "banana", "carrot", "donut"]
for item in shopping_cart:
    print(f"For Loop Checkout, item: {item}")

# For Loop through a Dictionary
# It's like an office directory - we go through each entry!
office_directory = {"Amy": "Accounting", "Bob": "Business", "Charlie": "Customer Service"}
for person, department in office_directory.items():  # .items() gets us both the key and value!
    print(f"For Loop Directory, person: {person} | department: {department}")

## While Loop
# It's like waiting in line - as long as there are people (condition is True), keep waiting!
people_in_line = 4
while people_in_line > 0:  # While there are people in line...
    print(f"While Loop: Waiting in line, people left: {people_in_line}")
    people_in_line -= 1  # One person gets through, so the line gets shorter!

## Break
# It's like a fire drill - stop everything immediately!
for step in range(1, 5):
    if step == 3:  # If we're on step 3...
        print("Break: Fire drill! Stop dancing!")
        break  # Stop the loop!
    print("Break Dance, step:", step)

## Continue
# It's like a minor stumble - we just keep going!
for step in range(1, 5):
    if step == 3:  # If we're on step 3...
        print("Continue: Oops! A stumble. But the dance goes on!")
        continue  # Skip the rest of this loop and start the next one!
    print(f"Break Dance, step: {step}")



### 10. Functions
print("\n--- Welcome to the Function Factory! ---\n")

# Functions are like machines in a factory. You design a machine (create a function) to do a specific task, and then you can
# use that machine over and over again to perform that task. This saves us time and helps keep our code clean and efficient.
# Let's start simple and build our first machine!

def greeting_machine():  # We've built a machine that simply greets the world!
    return "Hello, World!"

# The 'return' in a function is like the final product from our machine. It gives back a result, which could be a number, 
# string, list, etc. If no 'return' statement is specified, it simply returns None. 

# Now, let's use our greeting machine!
greeting = greeting_machine()  # Our machine greets the world!
print(f"Greeting Machine says: {greeting}")

# Feeling confident? Let's build a more advanced machine!

def multiplication_machine(x, y):  # This time we've built a machine that multiplies two numbers!
    return x * y

# Meet function arguments (x, y). They are like the raw materials for our machine!
# We can change these materials each time we run the machine to get different outputs. This makes our machine versatile!

# Let's put our advanced machine to work!
result = multiplication_machine(5, 3)  # Our machine multiplies 5 and 3 to give us 15!
print(f"Multiplication Machine in action: {result}")