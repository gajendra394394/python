itemID = input("enter id's:")
bucket = itemID[0]
for item in itemID:
    if item > bucket:
        bucket = item
print(bucket)