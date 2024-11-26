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

