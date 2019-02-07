arr = [4, 10, 22, 35, 36, 57, 65, 71, 79, 83, 87, 89, 90, 91, 93]

def bSearch(n):

    high = len(arr) - 1
    low = 0
    mid = (high + low)/2

    print mid

    while not (low + 1 > high):
        mid = (high + low)/2
        print("new mid", low, '.', high, '=', mid)

        if low + 1 == high:
            if n == arr[mid]:
                print "Found at position " + str(mid)
                return
            elif n == arr[mid+1]:
                print "Found at position " + str(mid+1)
                return
        else:
            if n > arr[mid]:
                low = mid
            elif n < arr[mid]:
                high = mid
            else:
                print "Found at position " + str(mid)
                return
    print "not found"

bSearch(34)