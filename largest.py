n=int(input("enter the number:"))
largest=0
for i in range(1,n+1):
    num=int(input("enter the number:"))
    if num>largest:
        largest=num
    print(largest)