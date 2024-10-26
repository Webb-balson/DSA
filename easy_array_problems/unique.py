def find_single(arr):
    n = len(arr)

    x = 0

    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1

        if count == 1:
            return i
        
    return -1

if __name__ == "__main__":
    arr = [2,3,5,4,5,3,4]
    print(f"Single ocurencce of element is : {find_single(arr)}")

