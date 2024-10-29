def fix_array(arr):
    n = len(arr)
    vec = [-1]*n

    for i in range(n):
        if arr[i] != -1:
            vec[arr[i]] = arr[i]

    return vec

arr = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
print(fix_array(arr))