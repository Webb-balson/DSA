def find_min(arr):
    n = len(arr)

    res = arr[0]

    for i in range(1, n):
        res = min(res, arr[i])

    return res

arr = [5,6,1,2,3,4]
print(find_min(arr))