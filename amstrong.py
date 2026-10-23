n=int(input("Enter a number: "))
sum=0
while (n!=0):
    r=n%10
    sum+=(r*r*r)
    n=n//10
print(sum)
if (sum==n):
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")