def fix_array(arr):
    n = len(arr)

    new = [0]*n

    for i in range(n):
        if i in arr:
            new[i] = i
        else:
            new[i] = -1

    return new

arr = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
print(fix_array(arr))