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
color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')

if color == 'green':
    print (f'User has chosen the color {color}.')
elif color == 'yellow':
    print (f"User's input was {color}.")
elif color == 'red':
    print (f"The input selected by the user was {color}.")
else:
    print(f'The color {color} is not apart of the original selection.')

#/-----------------------------------------------/#


