# 73.	Convert binary to decimal using loops.
binary_str = "1010"
decimal = 0
power = 0

for digit in binary_str[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

print(decimal)