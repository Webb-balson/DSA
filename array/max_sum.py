import sys

INT_MIN = -sys.maxsize - 1

def max_sum(arr,n,k):
    """
    Time complexity: O(n^2)
    """
    max_sum = INT_MIN

    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i+j]

        max_sum = max(current_sum, max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [1,4,2,10,2,3,1,0,20]
    k = 4

    n = len(arr)
    result = max_sum(arr,n,k)
    print(f"The maximum sum of all subarrays: {result}")