#automorphic numbers : 5**2=25, 6**2=36 , 25**2=625


num = int(input("Enter a number: \n"))


#find number of digits in num 
n = len(str(num))

#compute square
sqr = num**2

#Extract last n digits from the square
last = sqr%(10**n)

#compare last n digits with the input number
if last == num:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")