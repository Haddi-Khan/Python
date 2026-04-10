# 20.	Count_Number_Digits in a given number.
n = int(input("Enter any number: "))
count=0
if n==0:
    count=1
while n>0:
    n=n//10
    count +=1
print (count)