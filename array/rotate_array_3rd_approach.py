def rotate_array(arr, d):
    n = len(arr)

    # Handle case when d>n
    d = d%n

    # Reverse the entire array
    arr.reverse()

    # Reverse the first d elements
    arr[:d] = reversed(arr[:d])

    # Reverse the remaining n-d elements
    arr[d:] = reversed(arr[d:])

    print(arr)

arr = [1,2,3,4,5,6,7]
d = 3
rotate_array(arr,d)

