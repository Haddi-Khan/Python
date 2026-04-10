arr=[20,30,40,50,10,60]
max_value=arr[0]
for i in range (1,len(arr)):
    if arr[i]>max_value:
        max_value=arr[i]
print("max_value",max_value)