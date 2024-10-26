

def miss_reap(arr,n):

    visited = [False] * (n + 1)
    repeating = -1
    missing = -1

    for i in range(n):
        if visited[arr[i]]:
            repeating = arr[i]
        else:
            visited[arr[i]] = True

    for i in range(1, n+1):
        if not visited[i]:
            missing = i
            break
    
    print(f"Repeating : {repeating}")
    print(f"Missing : {missing}")

arr = [7,3,4,5,5,6,2]
miss_reap(arr, len(arr))

