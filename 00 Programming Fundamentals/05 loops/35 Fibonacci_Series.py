# 35.	Print Fibonacci series up to N terms.
num=int(input("enter any number "))
a,b=0,1
p=0
while p<=num:
    print(a,end="")
    c=a+b
    a=b
    b=c
    p=p+1