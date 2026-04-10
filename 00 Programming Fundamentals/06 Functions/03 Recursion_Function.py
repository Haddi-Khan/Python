def factorical(n):
    if n == 0 or n == 1:
        return 1
    else:
      return n* factorical (n-1)
a=int(input("enter any number: "))
print("your factorical for:",a,"is",factorical(a))