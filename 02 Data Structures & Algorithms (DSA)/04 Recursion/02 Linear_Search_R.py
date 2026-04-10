def linear_search (arr,target,index=0):
    if index == len(arr):
        return -1
    if arr[index]== target:
        return index
    return linear_search(arr,target,index+1) 
arr = [1,2,4,3,5,6]
print (linear_search(arr,6))
              


    
            