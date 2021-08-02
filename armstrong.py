a=[int(i) for i in input ().split()]
b=a.count(max(a))
for i in range (b):
    a.remove(max(a))
c=a.count(max(a));
for i in range (c):
    a.remove(max(a))
        
print(a)
print(max(a))


