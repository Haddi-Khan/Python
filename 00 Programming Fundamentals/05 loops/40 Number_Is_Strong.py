# 40.	Check if a number is strong (sum of factorial of digits = number).
n = int(input("Enter a number: "))
temp = n  
sum = 0
while n > 0:
    digit = n % 10    
    fact = 1
    j = 1
    while j <= digit:
        fact = fact * j
        j = j + 1
    
    sum = sum + fact 
    n = n // 10       

if sum == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")             