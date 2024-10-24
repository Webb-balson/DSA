def reverseArray(arr):
    n = len(arr)
    # result = []
    # for i in range(n-1,-1,-1):
    #     result.append(arr[i])
    # print(result)

    # Using two pointer
    # left = 0
    # right = n-1
    # while left<right:
    #     arr[left], arr[right] = arr[right], arr[left]

    #     left += 1
    #     right -= 1

    # print(arr)

    # By swapping elements
    for i in range(int(n/2)):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    print(arr)

def reverse_array_rec(arr, l, r):
    if l >= r:
        return
    
    # swap the elements at the ends
    arr[l], arr[r] = arr[r], arr[l]

    # Recur for the remaining array
    reverse_array_rec(arr, l+1, r-1)

if __name__ == "__main__":

    arr = [1,2,3,4,5,6]
    # reverseArray(arr)

    reverse_array_rec(arr, 0, len(arr)-1)
    print(arr)
