# Python implementation of converting
# a string into a dictionary

# initialising first string
str1 = "Jan, Feb, March"
str2 = "January | February | March"

# splitting first string
# in order to get keys
keys = str1.split(", ")

# splitting second string
# in order to get values
values = str2.split("|")

# declaring the dictionary
dictionary = {}

# Assigning keys and its
# corresponding values in
# the dictionary
for i in range(len(keys)):
	dictionary[keys[i]] = values[i]

# printing the generated dictionary
print(dictionary)
