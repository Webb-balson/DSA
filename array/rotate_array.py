def rotate(arr,d):
    n = len(arr)
    
    for _ in range(d):

        last = arr[n-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last

    print(arr)

arr = [1,2,3,4,5,6]
d = 2
rotate(arr,d)