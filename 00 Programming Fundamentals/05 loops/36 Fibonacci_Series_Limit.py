# 36.	Print Fibonacci_series_limit.
num=int(input("enter any number "))
a,b=0,1

while a<=num:
    print(a,end="")
    c=a+b
    a=b
    b=c
    
if num < 10:
    print("Limit breach: number too small")