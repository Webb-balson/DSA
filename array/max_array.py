def largest(arr, n, i):

    # For last index return the element
    if (i == n-1):
        return arr[i]

    # Find the max from rest of array
    recMax = largest(arr,n, i+1)

    # Compare with i-th element and return
    return max(recMax, arr[i])

if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808, 2]
    n = len(arr)

    print(f"Largest in given array is {largest(arr, n, 0)}")