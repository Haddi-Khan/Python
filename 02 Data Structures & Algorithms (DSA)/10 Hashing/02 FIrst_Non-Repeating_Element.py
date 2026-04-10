arr = [1,2,2,3,3,3,3]
freq ={}
for x in arr:
    freq[x] = freq.get(x, 0) + 1 
for x in arr:
    if freq[x] == 1:
        print(x)
        break
