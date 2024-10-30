def product(arr):
    n = len(arr)
    new = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if arr[i] == arr[j]:
                continue
            else:
                prod *= arr[j]

        new.append(prod)

    return new

arr = [10, 3, 5, 6, 2]
print(product(arr))