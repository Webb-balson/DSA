"""
Time Complexity: O(3*n) = O(n) as the loop is iterated only once
Auxilary space = O(1) as no extra space is required

"""

def largest_three_element(arr):
    n = len(arr)

    first = -1
    second = -1
    third = -1

    for i in range(n):
        if arr[i] > first:
            first = arr[i]

    for i in range(n):
        if arr[i] > second and arr[i] != first:
            second = arr[i]

    for i in range(n):
        if arr[i] > third and arr[i] != first and arr[i] != second:
            third = arr[i]

    return [first, second, third]

if __name__ == "__main__":
    arr = [12,45,13,67,67,45,99,99,52]
    print(f"Largest Three Distinct Element: {largest_three_element(arr)}")