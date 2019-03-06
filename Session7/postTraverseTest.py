a = [5, 7, 6, 9, 11, 10, 8]

def postTest(arr):
    if len(arr) <= 3:
        if arr[0] < arr[1]:
            return 0
        else: 
            return 1
    else:
        arr.pop(len(arr)-1)
        if not arr[int((len(arr)-1)/2)] < arr[int(len(arr)-1)]:
            return 1 + postTest(arr[0: int(len(arr)/2)]) + postTest(arr[int(len(arr))/2: 0])
        else:
            return 0 + postTest(arr[0: int(len(arr)/2)]) + postTest(arr[int(len(arr)/2): 0])
        
print(postTest(a))
    # if len(arr) == 1:
    #     return arr[len(arr)-1]
    # else:
    #     arr.remove(len(arr)-1)
    #     return postTest([:len(arr)/2]) < postTest([len(arr/2):])