"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
# we need to typecast the string var y to a n integer using the int function 
int_y = int(y)
#after converting y add the result 
result = x + int_y
# or do it all in one line 
one_line_result = int(y) + x 

print(result)
print(one_line_result)

# Write a print statement that combines x + y into the string value 57
# now we need to do the opposite of above - instead of y being typcast into a integer, we must convert x to a string 
str_x = str(x)
string = str_x + y 
# or do it in one line 
one_line_string = str(x) + y 

print(string)
print(one_line_string)
