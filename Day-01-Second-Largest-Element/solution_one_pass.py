def getSecondLargest(arr):
    if len(arr) < 2:
        return -1
    largest = -1
    secondLargest = -1
    for x in arr:
        if x > largest:
            secondLargest = largest
            largest = x
        elif x < largest and x > secondLargest:
            secondLargest = x
    return secondLargest
