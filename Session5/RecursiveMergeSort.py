arr = [62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12, 62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12]

def rMerge(_arr):
    if (len(_arr) == 1):
        return _arr
    else:
        return merge(rMerge(_arr[: int(len(_arr)/2)]), rMerge(_arr[int(len(_arr)/2):]))

def merge(f_arr, s_arr):
        # print('First array', f_arr)
        # print('Second array', s_arr)
        _arr = []

        while( len(f_arr) > 0 or len(s_arr) > 0):
            if( len(f_arr) == 0 and len(s_arr) != 0 ):
                while len(s_arr) != 0:
                    _arr.append(s_arr.pop(0))
            elif( len(f_arr) != 0 and len(s_arr) == 0 ):
                while len(f_arr) != 0:
                    _arr.append(f_arr.pop(0))
            elif( len(f_arr) != 0 and len(s_arr) != 0 ):
                if f_arr[0] > s_arr[0]:
                    _arr.append(s_arr.pop(0))
                else:
                    _arr.append(f_arr.pop(0))
        
        # print _arr
        return _arr

print(rMerge(arr))