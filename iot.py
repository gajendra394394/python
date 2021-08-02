n = int(input('Enter the total no. of students.')) 

ls = [] 
z = []  
for i in range(0, n): 
    x,y = input("Enter the student name and it's percentage: ").split() 
    ls.append((y,x)) 
    z.append((x,y))
      
ls = sorted(ls, reverse = True) 
  
print('Sorted list of students according to their marks in descending order') 
  
for i in ls: 
    print(i[1], i[0])

z = sorted(z) 
  
print('Sorted list of students according to their alphabetical order') 
  
for i in z: 
    print(i[0], i[1])
