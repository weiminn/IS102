arr = [4, 10, 22, 35, 36, 57, 65, 71, 79, 83, 87, 89, 90, 91, 93]

def bSearch(n):

    high = len(arr) - 1
    low = 0
    mid = int((high + low)/2)

    print (mid)

    while (low <= high):
        mid = int((high + low)/2)
        print("new mid", low, '.', high, '=', mid)

        if n > arr[mid]:
            low = mid + 1
        elif n < arr[mid]:
            high = mid - 1
        else:
            print("Found at position " + str(mid))
            return
    print("not found")

bSearch(10)