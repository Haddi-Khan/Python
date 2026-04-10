n=int(input("enter a number that you want to find "))
arr = [1,2,3,4,5,2,3,2,2,2,4,5,3,5,4,4,1,1,2,3,4,5,6,7,4,2,2,3,4,5,3]
count = 0
for values in arr:
    if values == n:
        count +=1
print (count)

