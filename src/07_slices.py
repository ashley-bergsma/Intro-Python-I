"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
# print("Second element", a[1:2])

# Output the second-to-last element: 9
# print("Second to last:", a[-2:-1])

# Output the last three elements in the array: [7, 9, 6]
# print("Last three", a[3:])

# Output the two middle elements in the array: [1, 7]
# print("Middle Slice", a[])

# print("Approaching this differently: ", a.pop(len(a)-1)//2)
# Why did I get this result?

# Output every element except the first one: [4, 1, 7, 9, 6]
#print()

# Output every element except the last one: [2, 4, 1, 7, 9]
#print()

# For string s...

#s = "Hello, world!"

# Output just the 8th-12th characters: "world"
#print()


month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]

word_count = len(month_list) # retrieves the number of strings in the list 
half_count = int(word_count/2) # divides the length of word_count by 2 (for 6) and cast as a integer

# First - Get the length of the array 
# Second - Divide that by 2 (provided the array is of an even number)
# Third take a slice that is the first half 

print(word_count)
print(half_count)

first_half = month_list[ :half_count] # takes a slice of the 0th element up to the half_count (which is 6)
print(first_half)

word_count = len(first_half)
middle_start = word_count//2 # two /'s cast to an integer for us?
print("middle_start: ", middle_start)

loose_var = middle_start + half_count
print("loose_var: ", loose_var)

middle_half = month_list[middle_start : middle_start+half_count]
# the middle of the month list is located at the month_list[3 : 9] starting at index 3 up to but not including 9 
print("Middle Half: ", middle_half)

# Not quite sure where I was going with this - will probably come back later to think on it. 