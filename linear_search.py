def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1


arr = [4, 2, 7, 1, 9, 5]
target = 7
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")