import sys

def closet_pair(arr):
    n = len(arr)

    res = sys.maxsize

    for i in range(n):

        x = arr[i]

        left, right = i+1, n-1

        while left < right:
            mid = (left + right)//2

            curr = arr[mid] + x

            if curr == 0:
                return 0
            
            if abs(curr)<abs(res):
                res = curr

            if curr < 0:
                left = mid + 1
            else:
                right = mid -1

    return res

arr = [-10, -3, 0, 5, 9, 20]
print(closet_pair(arr))