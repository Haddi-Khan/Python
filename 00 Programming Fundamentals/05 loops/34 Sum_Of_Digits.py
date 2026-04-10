# 34.	Find the sum of digits of a number until it becomes a single digit.
n = int(input("Enter a number: "))
while n >= 10:         
    total = 0
    while n > 0:        
        digit = n % 10
        total += digit
        n = n // 10
    n = total          
print("Single digit sum is:", n)