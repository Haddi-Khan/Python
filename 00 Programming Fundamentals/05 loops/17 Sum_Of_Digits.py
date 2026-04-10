# 17.	Print the sum of digits of a number using a loop.
n = int(input("Enter any number: "))
total = 0
while n > 0:
    digit = n % 10     
    total += digit     
    n = n // 10         
print("Sum of digits =", total)