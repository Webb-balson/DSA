def binary_search(arr, left, right, target):

    while left<right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            return True
        elif arr[mid]<target:
            left = mid + 1
        elif arr[mid]>target:
            right = mid -1
    
    return False

def two_sum(arr, target):
    n = len(arr)

    arr.sort()

    for i in range(n):
        complement = target - arr[i]

        if binary_search(arr, i+1, n-1, complement):
            return True
    
    return False

arr = [0,-1,2,-3,1]
print(two_sum(arr, -2))

