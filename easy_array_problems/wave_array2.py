def wave_arr(arr):
    n = len(arr)

    for i in range(0,n, 2):
        if i>0 and arr[i]<arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        
        if i< n-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    
    print(arr)

arr = [1,2,3,4,5,6,7]
wave_arr(arr)