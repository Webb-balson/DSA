def sum_pair(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return True
            
    return False

arr = [1,-2,1,0,5]
target = 0
print(sum_pair(arr, target))