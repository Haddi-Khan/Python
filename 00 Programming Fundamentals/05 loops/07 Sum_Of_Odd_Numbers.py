# 07.	Find the sum of odd numbers from 1 to N.
n =int(input("enter any number  "))
total =0
for i in range (1,n+1):
    if i %2 ==1:
        total +=i
print (total)