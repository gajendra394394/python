# Python3 code to demonstrate working of
# Test if string is subset of another
# Using issubset()

# initializing strings
str1 = input("enter main string:")
str2 = input("enter sub string:")

# printing original string
print("The original string is : " + str1)

# Test if string is subset of another
# Using issubset()
res = set(str2).issubset(str1)

# printing result
print((res))
