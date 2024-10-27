def even_and_odd(arr):
    n = len(arr)

    left = 0
    right = n-1

    while left < right:
        while(arr[left]%2==0 and left<right):
            left+= 1

        while(arr[right]%2==1 and left<right):
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1

    print(arr)

arr = [12,34,45,9,8,90,3]
even_and_odd(arr) 