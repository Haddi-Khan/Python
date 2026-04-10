# 28.	Count the number of odd digits in a number.
n=int(input("enter any digits "))
total =0
while n>0:
    digits=n%10
    if n%2==1:
        total = total+1
    n = n //   10
        
print(total)