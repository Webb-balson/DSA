
def prefix_sum(arr):
    
    n = len(arr)
    new = [0]*n
    new[0] = arr[0]
    for i in range(1,n):
        new[i] = new[i-1] + arr[i]
    
    return new

if __name__ == "__main__":
    arr = [10,20,10,5,15]
    result = prefix_sum(arr)

    print(f"The Prefix sum is : {result}")
