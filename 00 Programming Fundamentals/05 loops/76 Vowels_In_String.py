# 76.	Count vowels in a string using a loop.
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)