"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Objective: # Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Walkthrough and Learn: #
print("The string is %s" % z)
# The % is followed by s - for string 
# after the closing bracket the % is referenced again, followed by the variable it's calling 
# With the String Modulo Operator you control the output formatting! If you cast as a string (%s) the output will be a string. 
print("The string is %s" % x)
# This shows that 10 was converted to a string and printed with the message. 
# Referencing Multiple # 
# When we give more than one variable, regardless of type, at the end of the command we need to pass a Tuple containing the variables we want to substitute in the order that we want to substitute them 
print("x is %d, the string is %s" % (x, z))
# Now the % is followed by a d - for an integer(digit) - this will be a whole number 
print("Key-Pairs Method: ","x is %(x)d, y is %(y)f, z is '%(z)s'" % {"x": x, "y": y, "z":z})
# Key-Pairs Method: # 
# To reference the variables by name within the format string (and avoid the possible confusion of order in a tuple) 
# Using the f after % indicates the type is a Float 
# Using this method, following the String Modulo Operator, you have to pass a dictionary of key-value pairs

# Notes: 
# also known as the String Modulo Operator 
# This operator is 'overloaded' by the string class - thus its name. 
# not in common use, but good to be familiar with if you run into legacy code 

# Use the 'format' string method to print the same thing
print("Format String Method: ","x is {}, y is {}, z is '{}'".format(x, y, z))
# Format String Method: #
# This method doesn't require any direct referencing in the string
# The string is followed by the .format() method
# We pass Positional Arguments into the format method. We can reference them by using their positional references, otherwise Python does them in order
print("Changed the Positions: ","x is {1}, y is {2}, z is '{0}'".format(x, y, z))
# The positional arguments are wrapped in a Tuple and can be directly re-arranged how we need them. 

# Finally, print the same thing using an f-string
print("F-String Method: ", f"x is {x}, y is {y}, and z is '{z}'")
# F-String Method: #
# This method is more current, and straightforward. You don't need to specify the datatypes, they're referenced right inside the Formatted String 
# Python handles this under the hood? 