"""
Soting takes O(n*logn) time and traversing takes O(n) time
So total time complexity = (n*logn + n) = O(n*logn)
Auxilary space: O(1), as no extra space is required.
"""

def second_largest(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-2, -1, -1):
        if arr[i] != arr[n-1]:
            return arr[i]
        
    return -1

if __name__ == "__main__":
    arr = [12, 13, 44, 2, 55, 55, 65, 65, 23]
    print(f"Second Largest Number is: {second_largest(arr)}")