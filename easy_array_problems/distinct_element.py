"""
Naive Approach
Time Complexity: O(n^2)
Auxilary Space: O(n)
"""

def find_distinct(arr):
    n = len(arr)
    res = []

    for i in range(n):

        # check if this element is included in the result
        j = 0

        while j<i:
            if arr[i] == arr[j]:
                break
            j += 1

        if i == j:
            res.append(arr[i]) 

    return res

if __name__ == "__main__":
    arr = [12,10,9,45,2,10,10,45]
    res = find_distinct(arr)
    print(f"The distinct elements are: {res}")