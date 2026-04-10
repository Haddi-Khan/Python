file_name = "sample.txt"
with open(file_name, "r") as file:
    text = file.read()  
    words = text.split()
    print(f"Number of words in '{file_name}': {len(words)}")