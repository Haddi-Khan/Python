def is_pangram(sentence):
    sentence = sentence.lower() 
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    for char in alphabet:
        if char not in sentence:
            return False
    return True
sentence = input("Enter any sentence: ")
print("Is Pangram?:", is_pangram(sentence))