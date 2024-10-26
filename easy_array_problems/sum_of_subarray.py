def sum_of_array(arr):
    temp, result = 0,0
    n = len(arr)

    # Pick starting point
    for i in range(0,n):

        # Pick ending point
        temp = 0
        for j in range(i, n):
            temp += arr[j]
            result += temp

    return result

if __name__ == "__main__":
    arr = [1,2,3]
    result = sum_of_array(arr)
    print(f"The resulted sum is : {result}")
