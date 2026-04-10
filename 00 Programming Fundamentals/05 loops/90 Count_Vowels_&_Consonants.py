# 10.	Count Vowels & Consonants – For a given string, count vowels and consonants.
text = input("Enter a string: ")
v=0
c=0
vowels="AEIOUaeiou"
for ch in text:
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        if ch in vowels:
             v += 1
        else:
            c += 1     
print("Vowels:", v)
print("Consonants:", c)