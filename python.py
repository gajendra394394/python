d={'gaju':123,'baba':8908,'moma':90909 ,'hue':757};
ur=input("enter user name:");
for key in d :
    if key == ur:
        pd=input("enter password:");
    if d[key]==pd:
        print("logged in")
        break
    else:
         print('Invalid password')
         break
else:
    print('Invalid user')
