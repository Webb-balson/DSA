"""
Time Complexity: O(nlogn)
Auxilary Space: O(1)
"""
def wave_arr(arr):
    n = len(arr)

    arr.sort()

    i = 0
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)

arr = [1,2,3,4,5,6,7]
wave_arr(arr)