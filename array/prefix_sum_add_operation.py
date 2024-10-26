
if __name__ == "__main__":

    n = 5
    m =3
    q = [[2,4],[1,3],[1,2]]

    arr = [0 for i in range(5)]

    # for i in range(m):
    #     a,b = q[i][0], q[i][1]
    #     for i in range(a-1,b+1):
    #         arr[i] += 100

    # Efficient approach
    for i in range(m):
        a,b = q[i][0], q[i][1]
        arr[a-1] += 100
        arr[b] -= 100

    # new = [0]*n
    # new[0] = arr[0]
    # for i in range(1,n):
    #     new[i] = new[i-1] + arr[i]

    for i in range(1,n):
        arr[i] += arr[i-1]

    print(max(arr))