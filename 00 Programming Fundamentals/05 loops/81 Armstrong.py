n = int(input("Enter how many numbers: "))
largest = float('-inf')
second_largest = float('-inf')
i = 0
while i < n:
    num_str = input("Enter number: ")
    if num_str.strip() == "":   
        print("Please enter a valid number!")
        continue
    num = int(num_str)   
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
    i = i + 1
if second_largest == float('-inf'):
    print("No second largest number exists.")
else:
    print("The second largest number is:", second_largest)