def two_sum(arr, target):
    n = len(arr)

    arr.sort()

    left = 0
    right = n-1

    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1

    return False

arr = [0,-1,2,-3,1]
print(two_sum(arr, -2))