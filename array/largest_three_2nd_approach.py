"""
Time Complexity: O(n) as the arr in traversed only once
Auxilary space: O(1), as no extra space is needed
"""


def largest_three_element(arr):

    n = len(arr)

    # There should be atleast three elements
    if n<3:
        print("Invalid Input")
        return

    first = second = third = float('-inf')

    for i in range(n):
        if arr[i]>first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i]!=first:
            third = second
            second = arr[i]
        elif arr[i]>third and arr[i]!=first and arr[i]!=second:
            third = arr[i]

    return [first,second,third]

if __name__ == "__main__":
    arr = [12,45,13,67,67,45,99,99,52]
    print(f"Largest Three Distinct Element: {largest_three_element(arr)}")