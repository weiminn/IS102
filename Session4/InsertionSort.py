arr = [62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12, 62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12]

def iSort():
    i = 1
    while i < len(arr):
        j = i
        while (arr[j] < arr[j-1]) and j >= 0:
            print(arr[j], arr[j-1])
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
        i += 1

print arr
iSort()
print arr