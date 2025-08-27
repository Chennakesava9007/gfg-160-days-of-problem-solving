def findMajority(arr):
    n = len(arr)
    res = []

    for i in range(n):
        
        # Count the frequency of arr[i]
        cnt = 0
        for j in range(i, n):
            if arr[j] == arr[i]:
                cnt += 1
        
        # Check if arr[i] is a majority element
        if cnt > (n // 3):
            
            # Add arr[i] only if it is not already
            # present in the result
            if len(res) == 0 or arr[i] != res[0]:
                res.append(arr[i])
        
        # If we have found two majority elements, 
        # we can stop our search
        if len(res) == 2:
            if res[0] > res[1]:
                res[0], res[1] = res[1], res[0]
            break

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ") #output : 1 2 

# Time : O(n^2)
# Space : O(1)