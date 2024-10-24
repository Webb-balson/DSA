"""
Auxilary space: O(n), because we are maintaining a hash set to store items
"""

def remove_dup(arr):
    # new = []
    # arr.sort()
    # return list(set(arr))

    # new_set = set()
    # for i in arr:
    #     new_set.add(i)

    # return new_set

    n = len(arr)
    arr.sort()
    idx = 1
    for i in range(1,n):
        if arr[i] != arr[i -1]:
            arr[idx] = arr[i]
            idx = idx +1

    return idx


if __name__ == "__main__":
    arr = [12,11,45,23,1,56,1]
    size = remove_dup(arr)
    print(arr)
    print(size)
    for i in range(size):
        print(arr[i], end=" ")