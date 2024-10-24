
def is_sorted(arr):

    is_sort = True
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            is_sort = True
        else:
            is_sort = False

    if is_sort:
        print("Array is sorted")
    else:
        print("Array is not sorted")

# 2nd Approach
def array_sorted_or_not(arr, n):
    """
    Time complexity: O(n)
    Auxilary space: O(n) for Recursion call stack
    """
    # Best case
    if (n==0 or n==1):
        return True
    
    return (arr[n-1]>=arr[n-2] and array_sorted_or_not(arr, n-1))

if __name__ == "__main__":
    arr = [12,45,62,4,3,33,33,21]
    # arr = [1,2,3,4,5,5,6]
    is_sorted(arr)
    print(array_sorted_or_not(arr, len(arr)))