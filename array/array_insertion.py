import array

def insert_element(arr, x, pos):
    n = len(arr) # Current length of the array
    if pos < 0 or pos > n:
        raise IndexError("Position out of range")
    
    # Create one more array with n+1 length
    new_arr = array.array(arr.typecode, [0]*(n+1))

    # Copy elements to new array
    for i in range(pos):
        new_arr[i] = arr[i]

    new_arr[pos] = x

    for i in range(pos, n):
        new_arr[i+1] = arr[i]

    return new_arr

# Example
arr = array.array('i', [1,2,3,4,5,6])
x = 10  # Element to be inserted
pos = 4 # New position of element in the array

new_arr = insert_element(arr, x, pos)
print(new_arr.tolist())