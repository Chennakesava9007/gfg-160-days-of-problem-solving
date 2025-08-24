def reverseArray(arr):
    n = len(arr)
    
    # Iterate over the first half 
    # and for every index i, swap
    # arr[i] with arr[n - i - 1]
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        
if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ") #output : 5 6 2 3 4 1


# Time Complexity: O(n), the loop runs through half of the array, so it's linear with respect to the array size.
# Auxiliary Space: O(1), no extra space is required, therefore we are reversing the array in-place.