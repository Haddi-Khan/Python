# 13.	Count how many numbers from 1 to 100 are divisible by 3.
count =0 
for i in range (1,101):
    if i%3 ==0:
        count +=1
        print (i)
print (count)