arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)

if n % 2 == 0:
    mid = n // 2
    print(arr[:mid])
    print(arr[mid:])
else:
    print("it cannot be divided equally")
