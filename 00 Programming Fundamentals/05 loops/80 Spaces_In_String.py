# 80.	Count spaces in a string.
s = "Hello World !"
count = 0

for ch in s:
    if ch == " ":
        count += 1

print(count)   