def find_min_diff(arr, m):
    n = len(arr)

    arr.sort()

    min_diff = float('inf')

    for i in range(n-m+1):
        diff = arr[i+m-1] - arr[i]

        if diff < min_diff:
            min_diff = diff

    return min_diff

arr = [7,3,2,4,9,12,56]
m = 3
print(find_min_diff(arr, m))