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
# print("The string is %s" % z)
# Walkthrough and Learn: #

# The % is followed by s - for string 
# after the closing bracket the % is referenced again, followed by the variable it's calling 
# With the String Modulo Operator you control the output formatting! If you cast as a string (%s) the output will be a string. 
print("The string is %s" % x)
# This shows that 10 was converted to a string and printed with the message. 
# Referencing Multiple # 
# When we give more than one variable, regardless of type, at the end of the command we need to pass a Tuple containing the variables we want to substitute in the order that we want to substitute them 
print("x is %d, the string is %s" % (x, z))
# Now the % is followed by a d - for an integer(digit) - this will be a whole number 
print("x is %(x)d, y is %(y)d, z is %(z)s")
# Notes: 
# also known as the String Modulo Operator 
# This operator is 'overloaded' by the string class - thus its name. 
# not in common use, but good to be familiar with if you run into legacy code 

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string