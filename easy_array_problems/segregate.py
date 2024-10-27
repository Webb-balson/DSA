def segregate0and1(arr):
    n = len(arr)

    count = 0

    for i in range(n):
        if arr[i] == 0:
            count += 1

    for i in range(0,count):
        arr[i] = 0


    for i in range(count, n):
        arr[i] = 1


    print(arr)

arr = [0,1,0,1,0,0,1]
segregate0and1(arr)