import array

def find_element(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i

    return -1 # If element not found in the array

def delete_element(arr, ele):
    # Find position of element to be deleted
    pos = find_element(arr, ele)

    if pos == -1:
        print("Element Not Found !!")

    new_arr = array.array(arr.typecode, [0]*(len(arr)-1))

    # Copy all the elements to the new array except the one to be deleted

    for i in range(pos):
        new_arr[i] = arr[i]

    for i in range(pos+1, len(arr)):
        new_arr[i-1] = arr[i]

    return new_arr

# Example
arr = array.array('i',[1,2,3,4,5,6,7])
ele = 4

print(f"Index of {ele}: {find_element(arr, ele)}")

# Delete the element
new_arr = delete_element(arr, ele)
print(f"Array after deletion: {new_arr.tolist()}")