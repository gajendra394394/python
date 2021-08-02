# Function to combine n arrays
	
def combineAll(input):
		
	# cast first array as set and assign it
	# to variable named as result
	result = set(input[0])
	
	# now traverse remaining list of arrays
	# and take it's update with result variable
	for array in input[1:]:
		result.update(array)
	
	return list(result)
	
# Driver program

	input = [[1, 2, 2, 4, 3, 6],
			[5, 1, 3, 4],
			[9, 5, 7, 1],
			[2, 4, 1, 3]]
print (combineAll(input))
