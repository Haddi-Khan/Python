arr = [10,20,30,40,50,60]
target = int(input("enter a number: "))
for i in range(len(arr)):
    if arr[i] == target:
        print ('target is found at index',i)
        # break
else:
    print ("not found")
    

