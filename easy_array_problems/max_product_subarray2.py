def max_array(arr):
    n = len(arr)

    # max product ending at current index
    cur_max = arr[0]

    # min product ending at current index
    cur_min = arr[0]

    # Overall max product
    max_prod = arr[0]

    for i in range(1, n):
        temp = max(arr[i], cur_max*arr[i], cur_min*arr[i])

        cur_min = min(arr[i], cur_max*arr[i], cur_min*arr[i])

        cur_max = temp

        max_prod = max(max_prod, cur_max)

    return max_prod

arr = [-2, 6, -3, -10, 0, 2]
print(max_array(arr))