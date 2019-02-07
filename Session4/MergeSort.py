arr = [62, 77, 18, 48, 64, 45, 34, 88]

def mSort():
    g = 1
    while g < len(arr):
        pairUp(g)
        g *= 2

def pairUp(g):
    i = 0
    while i < len(arr):
        j = i + 2 * g
        arr[i:j] = merge(i, g, arr[i:j])
        i = j

def merge(i, g, a):
        f_arr = a[: len(a)/2]
        s_arr = a[len(a)/2 :]
        _arr = []
        # print('First array', f_arr)
        # print('Second array', s_arr)

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
                elif f_arr[0] < s_arr[0]:
                    _arr.append(f_arr.pop(0))
        
        # print _arr
        return _arr

print arr
mSort()
print arr