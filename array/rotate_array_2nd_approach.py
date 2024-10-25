def rotate_array(arr, d):

    n = len(arr)
    # Handle case when d > n
    d = d%n

    # temp1 = []
    # temp2 = []

    # n = len(arr)
    # temp1 = arr[n-d:n]
    # temp2 = arr[0:n-d]

    # arr = temp1 + temp2

    # print(temp1)
    # print(temp2)
    # print(arr)

    """
    Below is the third approach
    """

    temp = [0]*n

    # Coping the last d elements in the front of temp
    for i in range(d):
        temp[i] = arr[n-d+i]

    # Coping the first n-d elements in the last of temp
    for i in range(n-d):
        temp[i+d] = arr[i]

    for i in range(n):
        arr[i] = temp[i]

    print(arr)

arr = [1,2,3,4,5,6]
d = 4
rotate_array(arr,d)
