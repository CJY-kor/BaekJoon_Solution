def binarySearch(array, value, low, high):
    if len(array) == 0:
        return False
    if low > high:
	    return False
    mid = int((low+high) / 2)
    if array[mid] > value:
        return binarySearch(array, value, low, mid-1)
    elif array[mid] < value:
        return binarySearch(array, value, mid+1, high)
    else:
        return mid

print(binarySearch([],0, 0, 0))