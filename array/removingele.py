arr = [1,2,3,4,5,6]
n = len(arr)
pos = 1

if 0 <= pos < n:
    for i in range(pos, n-1):
        arr[i] = arr[i+1]

    n = n - 1

    print("Element deleted.")
    print("Updated Array:", arr[:n])

