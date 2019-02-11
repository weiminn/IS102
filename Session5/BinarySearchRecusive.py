_arr = [4, 10, 22, 35, 36, 57, 65, 71, 79, 83, 87, 89, 90, 91, 93]

def bSearch(arr, n):

    high = len(arr) - 1
    low = 0
    mid = int((high + low)/2)

    print (mid)

    if n > arr[mid]:
        if(low < mid):
            bSearch(arr[mid+1:], n)
        else:
            print("not found")
    elif n < arr[mid]:
        if(low < mid):
            bSearch(arr[: mid], n)
        else:
            print("not found")
    else:
        print("Found", n)

bSearch(_arr, 96)