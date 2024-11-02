def product_except_self(arr):

    n = len(arr)

    c = 0
    prod = 1
    res = [0]*n

    for num in arr:
        if num == 0:
            c += 1
        else:
            prod *= num

    for i in range(n):
        if c>1:
            res[i] = 0
        elif c == 1:
            if arr[i] == 0:
                res[i] = prod
            else:
                res[i] = 0
        else:
            res[i] = prod // arr[i]

    return res

nums = [10, 0, 5, 6, 2]
result = product_except_self(nums)

print(" ".join(map(str, result)))