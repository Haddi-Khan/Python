# 29.	Reverse the digits of a number.
n=int(input("enter any number "))
rev=0
while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print (rev)   