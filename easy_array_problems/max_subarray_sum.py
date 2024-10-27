
def max_array(arr):
    res = arr[0]

    for i in range(len(arr)):
        currsum = 0

        for j in range(i, len(arr)):
            currsum = currsum + arr[j]

            res = max(res, currsum)

    return res

arr = [2,3,-8,7,-1,2,3]
print(max_array(arr))
