arr = [3, 7, 2, 9, 4]
count_even = 0
count_odd = 0
for values in arr:
    if values %2==0:
        count_even +=1
    else:
        count_odd +=1

print (count_even)
print (count_odd)