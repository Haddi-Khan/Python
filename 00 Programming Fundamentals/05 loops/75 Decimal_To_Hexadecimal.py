# 75.	Convert decimal to hexadecimal using loops.
n = 255
hex_digits = "0123456789ABCDEF"
hexa = ""

while n > 0:
    remainder = n % 16
    hexa = hex_digits[remainder] + hexa
    n //= 16

print(hexa)