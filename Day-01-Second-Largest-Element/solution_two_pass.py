def getSecondLargest(arr):
    if len(arr) < 2:
        return -1
    largest = -1
    secondLargest = -1
    for x in arr:
        if x > largest:
            largest = x
    for x in arr:
        if x != largest and x > secondLargest:
            secondLargest = x
    return secondLargest
