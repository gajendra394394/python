a=int(input("enter 1st number :"));
b=int(input("enter 2 nd number :"));
for i in range(1,a*b+1):
    if ((i%a==0) and (i%b==0)):
        print("LCM of the numbers is :",i);
        break