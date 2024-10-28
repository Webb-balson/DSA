def min_abs_sum_pair(arr):
    n = len(arr)

    res = arr[0] + arr[1]

    for i in range(n-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]

            if abs(sum) < abs(res):
                res = sum

    return res

arr = [1,60,-10,70,-80,85]
print(min_abs_sum_pair(arr))