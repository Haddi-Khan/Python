string= ["sara","zara","zain","ali"]
target=input("enter name: ")
for i in range (len(string)):
    if string[i]==target:
        print ("found at index",i)
        break
else:
    print("not f0und")