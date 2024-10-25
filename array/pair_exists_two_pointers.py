
def two_sum(arr, target):

    # sort the array
    arr.sort()

    left, right = 0, len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False


if __name__ == "__main__":
    arr = [0,-1,2,-3,1]
    target = -2

    result = two_sum(arr, target)
    print(f"Is the pair exists: {result}")