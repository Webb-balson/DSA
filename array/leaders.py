

def leaders(arr):
    n = len(arr)

    # for i in range(0, n-1):
    #     for j in range(i+1, n):
    #         if arr[i]>arr[j]:
    #             leader = True
    #         elif arr[i]<arr[j]:
    #             leader = False
    #             break
        
    #     if leader:
    #         print(arr[i])

    """
    # Below is the Correct solution
    # Time Complexity: O(n^2), as we are traversing the array twice
    
    """
    # result = []
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i]<arr[j]:
    #             break
    #     else:
    #         result.append(arr[i])

    # return result

    """
    Below is the effiecient approach
    Time Complexity: O(n), as we only traveresed the array once
    Auxilary space: O(1), as no extra space was needed
    """

    leader = arr[-1]
    result = []
    result.append(leader)
    for i in range(n-2, -1, -1):
        if arr[i]>=leader:
            result.append(arr[i])
            leader = arr[i]
    
    result.reverse()

    return result

if __name__ == "__main__":
    arr = [12,45,62,4,3,33,33,21]
    print(leaders(arr))