def find_single(arr):
    freq = {}

    # Store frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key,value in freq.items():
        if value == 1:
            return key
        
    return -1

if __name__ == "__main__":
    arr = [2,3,5,4,5,3,4]
    print(find_single(arr))