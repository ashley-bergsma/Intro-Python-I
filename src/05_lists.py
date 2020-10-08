# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

x.append(4)

print("Number One: ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

x.extend(y)

print("Number Two: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

x.pop(4)

print("Number Three: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.extend([99, 100])

print("Number Four: ", x)

# Print the length of list x
# YOUR CODE HERE

print("Length of X is: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

print("List Comprehension: ", [i * 1000 for i in x])

# List Comprehensions: # 
# Combine the creation or manipulation of an element and a for loop
# Python automatically takes care of appending for you!
# You can even add an IF at the end 

print("If i > 4: ", [i * 1000 for i in x if i > 4])
# i refers the original value of the list element.
# so in this case only 9, 10, 99 and 100 were multiplied and returned 

