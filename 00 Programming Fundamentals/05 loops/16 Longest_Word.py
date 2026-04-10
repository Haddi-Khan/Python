s = "Python is a programing language "
words = s.split()

long_word = ""
for word in words:
    
    if len(word) > len(long_word):
        long_word = word

print(long_word)
# 
# s = "my name is Abdul Haddi"
# words = s.split()

# max_length = max(len(word) for word in words)
# longest_words = [word for word in words if len(word) == max_length]

# print("Longest words:", longest_words)