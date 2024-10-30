def binary_search(arr, low, high, key):
    while low<=high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid -1

    return -1

def find_pivot(arr, low, high):
    while low<high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high)//2

        if arr[mid] > arr[high]:
            low = mid + 1

        else:
            high = mid

    return low

def pivoted_binary_search(arr,n, key):
    pivot = find_pivot(arr, 0, n-1)

    if pivot == 0:
        return binary_search(arr, 0, n-1, key)
    
    if arr[pivot] == key:
        return pivot
    
    if arr[0] <= key:
        return binary_search(arr, 0, pivot -1, key)
    
    return binary_search(arr, pivot + 1, n-1, key)

# arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# key = 3
arr = [4, 5, 6, 7, 0, 1, 2]
key = 0
print(pivoted_binary_search(arr, len(arr), key))