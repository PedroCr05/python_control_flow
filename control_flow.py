def falsy():
    boolean = False
    none_data_type = None
    zero_in_numeric_data_type = 0
    zero_in_float_data_type_too = 0.0
    empty_str = ''
    empty_li = []
    empty_tuple = ()
    # That's a new word! Might look into that later...
    empty_dictionary = {}
    # Same thing... why are they not called the same. I guess that'd be the same as why not call
    # print as console.log
    empty_range = range(0)
    # ooo a new function!

    print(boolean, none_data_type, zero_in_numeric_data_type, zero_in_float_data_type_too, empty_str, empty_li, empty_tuple, empty_dictionary, empty_range)

falsy()

# All though I would try and figure out how a if statement works. I will not do that... yet. regardless all of these are falsy values.
# Key note. Empty (parameters) and [arrays] were truthy in JS. In python however (tuple) and [list] are actually falsy if they're empty.

#/-----------------------------------------------/#

not_equal_to = "=!"
equal_to = "=="
greater_than = ">"
less_than = "<"
greater_than_or_equal_to = ">="
less_than_or_equal_to = "<="

print(8 == 8)
# True

print(8 == "7")
# False

print(8 != 8)
# False

print(8 != "8")
# True

print(8 > 8)
# False

print(8 >= 8)
# True

print(8 < 8)
# False

print(8 <= 8)
# True

JS_or_symbol = "||"
JS_and_symbol = "&&"

"""
Python's Or is just or while And is just and. Crazy right?

Here are some examples of how or works. Just a refresher!

Remember or & and returns the first truthy operand, or the last operand

or will always go for True
and will always target False
"""

print(True or False)
# prints: True

print(False or True)
# prints: True

print(False or False)
# prints: False

print('hello' or 0)
# prints: 'hello'

print(0 or 'hello')
# prints: 'hello'

print('hello' or 'tacos')
# prints: 'hello'

print(True and False)
# prints: False

print(False and True)
# prints: False

print('hello' and 0)
# prints: 0

print(0 and 'hello')
# prints: 0

print('hello' and 'tacos')
# prints: 'tacos'
"""
Do you see a pattern? It's basically almost an if statement. Precisely just a boolean. True or False

As well you can have more than 1 boolean statement if you'd like as well.
"""

print(True or True or True)
# prints: True

print(True or True or False)
# prints: True

print(True and True and True)
# prints: True

print(True and True and False)
# prints: False

# We can also sprinkle both in together as a condition too.
print(False or True and True)
# prints: True

print(not False)
# not here is actually from what I understand is like a bang operator. Returning the opposite of the value of truthy or falsy
# True

print(not "hello")
# False

#/-----------------------------------------------/#

floor = "sticky"
walls = "clean"
# notice the colon ':' after the conditional expression
# it indicates the start of the if block
if floor == "sticky":
    print("Clean the floor! It's sticky!")
    # this is where you would add more lines of code related to the condition
    # each line must be indented to be part of the 'if' block
    print("If I am being read. That means I am correctly indented. Meaning I am inside the scope of the walls conditional.")

# unindented code indicates that we have returned to normal code execution
print("This will always print, it's not inside of an if block!")

# parentheses are not required around the conditional expression
if walls == "sticky":
    print("Clean the walls! They're sticky!")

print("If I'm not indented. I am not within the scope of the walls conditional.")
"""
I did already get the exposure to this with doing def which is functions in JS. Indenting MATTERS in python
We don't use curly or parenthesis 
"""

val = 3
# val = 1

# if path
if val == 1:
    print('val is one')
# else path
else:
    print('val is not one')
    # prints: val is not one
    # since val is not 1, the else path is taken

if val == 1:
    print('val is one')
elif val == 2:
    print('val is two')
elif val == 3:
    print('val is three')
    # prints: val is three
    # since val is 3, this elif path is taken
else:
    print('not one, two, or three')
#/---------------[I do Section]------------------/#
# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# if color == 'green':
#     print (f'User has chosen the color {color}.')
# elif color == 'yellow':
#     print (f"User's input was {color}.")
# elif color == 'red':
#     print (f"The input selected by the user was {color}.")
# else:
#     print(f'The color {color} is not apart of the original selection.')

#/-----------------------------------------------/#

"""
 A JavaScript for loop
for (let i = 0; i < 10; i++) {
 do something ten times
}

JS's for loop
"""

names = ["Emily", "Jack", "Sophia", "Ethan"]

for name in names:
    print(name)

'''
let names = ["Emily", "Jack", "Sophia", "Ethan"];
for (name of names) {
  console.log(name);
}

This here is the same exact way of JS's for of.
Which I've never personally used or knew about.
Now I know.
'''

num = 1

while num <= 10:
    print(num)
    # prints the numbers 1 through 10
    num += 1

"""
Should be simple to see but this is a while loop right above.
"""

things = ["computer", "g-g-ghost", "chair", "spider", "desk"]

for thing in things:
    if thing == "g-g-ghost":
        print("Oh, that's just my ghost friend, carry on.")
        continue
    elif thing == "spider":
        print("Nope. Burn it down, no more.")
        break
    print(f"There is a {thing} in the room.")

#/---------------[I do Section]------------------/#

# list_of_colors = ["green", "yellow", "red"]
# color = input(f'Enter {list_of_colors}: ').lower()
# print(f'The user entered {color}')

# while color:
#     if color == 'green':
#         print (f'User has chosen the color {color}.')
#     elif color == 'yellow':
#         print (f"User's input was {color}.")
#     elif color == 'red':
#         print (f"The input selected by the user was {color}.")
#         continue
#     elif color != list_of_colors:
#         print(f'The color {color} is not apart of the original selection.')
#     elif color == 'quit':
#         print(f'You have {color} the program. Good bye! Beep Boop.')
#         break

'''
So clearly I'm doing this incorrectly but I'll leave this here so I can compare and see what I'm doing :b

Edit: Just realized that continue and break is like the concept of try and catch in JS. Not the same way but the purpose of what it does.

Gave up but would 100% want to see in the future if I can solve it the way I have it above.
'''

while True:
    color = input('Enter "green", "yellow", "red", or type "quit": ').lower()
    print(f'The user entered {color}')

    if color == 'green':
        print (f'User has chosen the color {color}.')
    elif color == 'yellow':
        print (f"User's input was {color}.")
    elif color == 'red':
        print (f"The input selected by the user was {color}.")
    elif color == 'quit':
        print ("You've shut down the program!")
        break
    else:
        print(f'The color {color} is not apart of the original selection.')

#/-----------------------------------------------/#

# time_of_day = 9
time_of_day = 13

morning = True if time_of_day < 12 else False
print(morning)
#True

# This is ternary for python

#/-----------------------------------------------/#

for num in range(5):
    print(num)
    # prints the integers: 0, 1, 2, 3, 4

# Range always starts with 0 if not predefined with a preset num

for even in range(4, 12, 2):
    print(even)
    # prints the integers: 4, 6, 8, 10

# range(Starting num, The limit num, by how many it counts)

nums = list(range(10))
print(nums)
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# You can attach functions onto range so it can add, For example here we are creating 10 elements inside a list

for num in range(5, 0, -1):
    print(num)
    # prints the integers: 5, 4, 3, 2, 1

# Negative numbers are a possibility (Stepping back). Pretty neat!