# Python Program to left rotate the array by d positions
# using Juggling Algorithm

import math

# Function to rotate array
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Calculate the number of cycles in the rotation
    cycles = math.gcd(n, d)

    # Process each cycle
    for i in range(cycles):
        
        # Start element of current cycle
        startEle = arr[i]
        
        # Start index of current cycle
        currIdx = i
        
        # Rotate elements till we reach the start of cycle
        while True:
            nextIdx = (currIdx + d) % n
            
            if nextIdx == i:
                break
            
            # Update the next index with the current element
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx
        
        # Copy the start element of current cycle at the last
        # index of the cycle
        arr[currIdx] = startEle


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, d)

    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ") #output : 3 4 5 6 1 2 

# Time Complexity: O(n), as all the cycles are independent and we are not visiting any element more than once.
# Auxiliary Space: O(1)