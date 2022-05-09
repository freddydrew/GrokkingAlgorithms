"""
Grokking Algorithms - Binary Search Function
Chapter 1. Introduction to Algorithms
"""

def BinarySearch(data,item):
    low = 0 #first idx 
    high = len(data) - 1 #last idx
    mid = (low + high)//2 #guess idx of thing
    numSteps = 0

    while low <= high:           
        if data[mid] < item:
            low = mid + 1
            mid = (low + high)//2 #int division to not get decimal
            numSteps += 1
        elif data[mid] > item:
            high = mid - 1
            mid = (low + high)//2
            numSteps += 1
        elif data[mid] == item:
            numSteps += 1
            return mid
        else:
            return None


exArray = range(0,1000)
idx = BinarySearch(exArray,6)
print(idx)