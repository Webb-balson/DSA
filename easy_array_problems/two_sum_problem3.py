# Wrong, re-visit again
# Using sorting and two pointer

def two_sum(arr):

    n = len(arr)

    arr.sort()

    left = 0
    right = n-1

    sum = arr[left] + arr[right]
    diff = abs(sum)

    while left<right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == 0:
            return True
        
        if abs(curr_sum) < abs(diff):
            diff = curr_sum
            sum_val = curr_sum

        elif abs(curr_sum) == abs(diff):
            sum_val = max(sum_val, curr_sum)

        if curr_sum > 0:
            j -= 1
        else:
            i += 1

    return sum_val

arr = [1,60,-10,70,-80,85]
print(two_sum(arr))