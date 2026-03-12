arr = [1,3,4,5,6]
n = len(arr)
arr.append(3)
for i in range(n,3,-1):
    arr [i] = arr[i-1];
arr[3]=0
print(arr)