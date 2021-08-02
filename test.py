l=[];
def rada (c):
    factorial =1;
    for i in range (1,c+1):
         factorial = factorial * i
         l.append(factorial);
    print(sum(l))
         
a=int(input())
rada(a)