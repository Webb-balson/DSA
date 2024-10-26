# Function to calculate the maximum profit

def max_profit(arr):
    n = len(arr)
    l_min = arr[0]
    l_max = arr[0]

    res = 0
    i = 0
    while i < n-1:

        # Find local minima
        while i < n-1 and arr[i] >= arr[i+1]:
            i += 1
        l_min = arr[i]

        # Find local maxima
        while i < n-1 and arr[i] <= arr[i+1]:
            i +=1
        l_max = arr[i]

        res += l_max - l_min

    return res

if __name__ == "__main__":
    arr = [100,180,260,310,40,535,695]
    res = max_profit(arr)

    print(f"Maximum profit earned: {res}")