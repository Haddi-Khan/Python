def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if is_anagram(word1, word2):
    print("Yes, they are anagrams.")
else:
    print("No, they are not anagrams.")