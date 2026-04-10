arr=[20,30,40,50,10,60]
min_value = arr[0]
for i in range (1, len (arr)):
    if arr[i]<min_value:
        min_value=arr[i]
print ("min_value",min_value)