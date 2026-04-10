# 27.Count the number of even digits in a number.
n = int(input("Enter any number: "))
count = 0

while n > 0:
    digit = n % 10       
    if digit % 2 == 0:   
        count = count+1
    n = n // 10          

print("Number of even digits:", count)