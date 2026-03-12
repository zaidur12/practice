arr = [ 1,2,3,4,5,6,7]
max = float('-inf')
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        i+=1
print(max)     