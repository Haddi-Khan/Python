# 37.	Count total number of factors of a number.
n=int(input("enter any number for the factor "))
count=0
i=1
while i<=n:
    if  n%i==0:
        count=count+1
    i=i+1
print (count)