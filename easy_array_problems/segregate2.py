def segregate0and1(arr):
    n = len(arr)
    left = 0
    right  = n-1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1

        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    print(arr)

arr = [0,1,0,1,1,1]
segregate0and1(arr) 