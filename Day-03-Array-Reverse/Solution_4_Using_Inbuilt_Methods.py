# function to reverse an array
def reverse_array(arr):
    arr.reverse()

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverse_array(arr)
  
    print(" ".join(map(str, arr))) #output : 5 6 2 3 4 1


# Time Complexity: O(n), the reverse method has linear time complexity.
# Auxiliary Space: O(1) Additional space is not used to store the reversed array, as the in-built array method swaps the values in-place.