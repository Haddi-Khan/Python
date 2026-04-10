# 39.	Check if a number is perfect.
n=int(input("enter a number "))
sum=0
i=1
while i<n:
    if n % i==0:
        sum=sum+i
    i=i+1
if sum==n:
        print("perfect")
else:
    print("NOT")
    