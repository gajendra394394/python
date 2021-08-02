def record(x,y,z):
  d={ }
  d['Name']=x
  d['Roll']=y
  d['Marks']=z
  return(d)
s=input('Enter Name: ')
r=int(input('Enter Roll Number: '))
m=float(input('Enter Marks: '))
p=record(s,r,m)
print(p)