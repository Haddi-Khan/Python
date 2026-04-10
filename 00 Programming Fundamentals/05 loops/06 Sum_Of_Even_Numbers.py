# 06.Find the sum of even numbers from 1 to N.
n=int(input("Enter any number for the sum " ))
total =0
for i in range (1,n+1):
    if i %2 ==0:
        total +=i
print (total)