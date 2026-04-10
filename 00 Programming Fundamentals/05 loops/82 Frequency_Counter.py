# 82.	Frequency Counter – Count how many times each character appears in a string.
text = input("Enter a string: ")
frequency = {} 
for char in text:      
    if char in frequency:   
        frequency[char] += 1
    else:                  
        frequency[char] = 1
for key in frequency:
    print(key, ":", frequency[key])