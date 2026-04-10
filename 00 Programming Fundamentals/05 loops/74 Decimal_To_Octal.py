# 74.	Convert decimal to octal using loops.
n = 65
octal = ""
while n > 0:
    remainder = n % 8
    octal = str(remainder) + octal
    n //= 8

print(octal)