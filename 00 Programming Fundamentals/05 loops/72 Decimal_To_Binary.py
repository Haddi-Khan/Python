# 72.	Convert decimal to binary using loops.
n = 13
binary = ""

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary  
    n //= 2

print(binary) 