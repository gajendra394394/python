s=input("enter string:");
for i in range (len(s)):
   
    if s.count(s[i])>1:
        print(s.find(s[i]),end=" ");
        
