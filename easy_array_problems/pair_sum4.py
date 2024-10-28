def two_sum(arr, target):
    n = len(arr)

    s = set()

    for number in arr:
        complement = target - number

        if complement in s:
            return True
        
        s.add(number)

    return False

arr = [0,-1,2,-3,1]
target = -2
print(two_sum(arr, target))