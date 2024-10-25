
def two_sum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True
    
    return False

if __name__ == "__main__":
    arr = [0,-1,2,-3,1]
    target = -2

    result = two_sum(arr, target)
    print(f"Is the target sum is available: {result}")
