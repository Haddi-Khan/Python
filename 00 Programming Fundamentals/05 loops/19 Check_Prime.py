# 19.	Check_Prime using a loop.
n = int(input("Enter any number: "))
if n <= 1:
    print(n, "is NOT a prime number")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break    
    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is NOT a prime number")
    
    