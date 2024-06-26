def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        

        if arr[mid] == target:
            return mid
        
        
        elif arr[mid] < target:
            left = mid + 1
        
        
        else:
            right = mid - 1
    
    
    return -1


arr = ['apple','banana','carrot','hyderabad','zebra']
target = 'hyderabad'
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")