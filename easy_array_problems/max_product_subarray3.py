def max_product(arr):
    n = len(arr)
    max_prod = float('-inf')

    # To store product from left to right
    left_to_right = 1

    # To store product from right to left
    right_to_left = 1

    for i in range(n):
        if left_to_right == 0:
            left_to_right = 1
        if right_to_left == 0:
            right_to_left = 1

        # calculating product from index left to right
        left_to_right *= arr[i]

        # calculating product from index right to left
        j = n-i-1
        right_to_left *= arr[j]

        max_prod = max(left_to_right, right_to_left, max_prod)

    return max_prod

arr = [-2, 6, -3, -10, 0, 2]
print(max_product(arr))