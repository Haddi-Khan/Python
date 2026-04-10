arr = [10,20,30,40,50,60]
target = 30
for i in range(len(arr)):
    if arr[i] == target:
        print ('target is found at index',i)
    else:
        print ("not found",i)