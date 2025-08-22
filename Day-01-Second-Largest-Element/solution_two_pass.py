# Python program to find the second largest element in the array
# using two traversals

# Function to find the second largest element in the array
def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # Finding the largest element
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    # Finding the second largest element
    for i in range(n):
        
        # Update second largest if the current element is greater
        # than second largest and not equal to the largest
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr)) #output : 34

# Time Complexity: O(2*n) = O(n), as we are traversing the array two times.
# Auxiliary space: O(1), as no extra space is required.