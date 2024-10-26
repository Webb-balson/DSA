# Python Program implementation for sliding window problem
"""
Optimized max sum of subarray by using sliding window technique
Time Complexity: O(n)
Auxilary Space: O(1)
"""
def max_sum(arr,k):
    n = len(arr)

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [1,42,2,10,2,3,1,0,20]
    k = 4
    result = max_sum(arr,4)
    print(f"The result sum is {result}")