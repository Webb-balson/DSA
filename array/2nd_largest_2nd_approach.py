"""
Time Complexity: O(2*n) = O(n), as we are traversing the array only once.
Auxilary space: O(1), as no extra space is needed.
"""

def second_largest(arr):
    n = len(arr)

    largest = -1
    sec_largest = -1

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
        # else:
        #     continue

    # for i in range(n):
    #     if arr[i] == largest:
    #         continue
    #     elif arr[i] > sec_largest:
    #         sec_largest = arr[i]
    #     else:
    #         continue

    # Optimising above for loop
    for i in range(n):
        if arr[i]>sec_largest and arr[i] != largest:
            sec_largest = arr[i]

    return sec_largest

if __name__ == "__main__":
    arr = [12,65,34,76,34,22,21]
    print(f"Second Largest: {second_largest(arr)}")