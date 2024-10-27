def segregate0and1(arr):
    n = len(arr)
    lef = 0 
    righ = n-1

    while lef < righ:
        if arr[lef] == 1:
            if arr[righ] != 1:
                arr[lef], arr[righ] = arr[righ], arr[lef]

            righ -= 1
        else:
            lef += 1

    print(arr)

arr = [0,1,0,1,1,1]
segregate0and1(arr)