# 78.	Reverse a string using a loop.
s = "hello"
rev = ""

for ch in s:
    rev = ch + rev   # prepend character

print(rev)  