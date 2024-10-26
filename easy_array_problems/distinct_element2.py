"""
Better approach than using nested loop
Time Complexity: O(nlogn), coz sorting takes O(nlogn) time
Auxilary Space: O(n)
"""
def find_distinct(arr):
    n = len(arr)
    res = []

    arr.sort()

    for i in range(n):
        if i == 0 or arr[i] != arr[i-1]:
            res.append(arr[i])

    return res

if __name__ == "__main__":
    arr = [12,10,9,45,2,10,10,45]
    res = find_distinct(arr)
    print(f"The distinct element in an array: {res}")

