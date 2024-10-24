def second_largest(arr):
    n = len(arr)
    largest = -1
    sec_largest = -1

    for i in range(n):
        if arr[i]>largest:
            sec_largest = largest
            largest = arr[i]
        elif arr[i]< largest and arr[i]>sec_largest:
            sec_largest = arr[i]
        
    return sec_largest

if __name__ == "__main__":
    arr = [12,65,34,76,76,34,22,21]
    print(f"Second Largest: {second_largest(arr)}")