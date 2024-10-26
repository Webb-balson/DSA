def find_missing(arr,n):
    summation = n * (n+1)//2

    arr_sum = sum(arr)

    missing_number = summation - arr_sum

    return missing_number

if __name__ == "__main__":
    arr = [1,2,3,5]
    n = 5

    print(find_missing(arr,n))