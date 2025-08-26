# Function to generate all possible permutations
def generatePermutations(res, arr, idx):

    # Base case: if idx reaches the end of array
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    # Generate all permutations by swapping
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recur for the next index
        generatePermutations(res, arr, idx + 1)

        # Backtrack to restore original array
        arr[idx], arr[i] = arr[i], arr[idx]

# Function to find the next permutation
def nextPermutation(arr):

    res = []

    # Generate all permutations
    generatePermutations(res, arr, 0)

    # Sort all permutations lexicographically
    res.sort()

    # Find the current permutation index
    for i in range(len(res)):

        # If current permutation matches input
        if res[i] == arr:

            # If it's not the last permutation
            if i < len(res) - 1:
                arr[:] = res[i + 1]

            # If it's the last permutation
            else:
                arr[:] = res[0]

            break

if __name__ == "__main__":

    arr = [2, 4, 1, 7, 5, 0]

    nextPermutation(arr)

    for x in arr:
        print(x, end=" ") #output : 2 4 5 0 1 7 


# Time : O(n! * n)
# Space : O(n! * n)